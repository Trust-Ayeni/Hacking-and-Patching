import aiohttp
import asyncio
import os
import argparse
import random
import time
import signal
import sys
import logging
from urllib.parse import quote_plus
from aiohttp import ClientTimeout
import gc

# ANSI escape codes for colors
COLOR_RED = '\033[91m'
COLOR_GREEN = '\033[92m'
COLOR_RESET = '\033[0m'

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class AsyncDirFileSearcher:
    def __init__(self, base_url, wordlist_path, extensions=None, max_concurrent_requests=11, max_retries=10, batch_size=40):
        self.base_url = base_url.rstrip('/')
        self.wordlist_path = wordlist_path
        self.extensions = extensions if extensions else []
        self.max_concurrent_requests = max_concurrent_requests
        self.max_retries = max_retries
        self.batch_size = batch_size
        self.found_paths = []
        self.should_exit = False

        # Set up signal handlers
        signal.signal(signal.SIGINT, self.handle_signal)
        signal.signal(signal.SIGTERM, self.handle_signal)

    def handle_signal(self, signum, frame):
        logging.info("Signal received. Exiting gracefully...")
        self.should_exit = True

    async def fetch(self, session, url, path):
        attempt = 0
        while attempt < self.max_retries:
            if self.should_exit:
                logging.info("Exit requested; cancelling fetch.")
                return

            try:
                async with session.get(url, timeout=ClientTimeout(total=65)) as response:
                    status = response.status
                    if status == 200:
                        if path.endswith('.zip'):
                            logging.info(f"{COLOR_GREEN}Found and downloadable: {url} (HTTP 200){COLOR_RESET}")
                        else:
                            logging.info(f"{COLOR_GREEN}Found: {url} (HTTP 200){COLOR_RESET}")
                        self.found_paths.append(url)
                    elif status == 403:
                        logging.warning(f"Forbidden: {url} (HTTP 403)")
                    elif status == 404:
                        logging.info(f"{COLOR_RED}Not Found: {url} (HTTP 404){COLOR_RESET}")
                    elif status == 429:  # Too Many Requests
                        delay = response.headers.get('Retry-After', 60)  # Use header if available
                        logging.warning(f"Rate limit hit: {url}. Retrying after {delay} seconds")
                        await asyncio.sleep(float(delay))
                    else:
                        logging.warning(f"Received unexpected status code {status} for {url}")
                    return
            except asyncio.TimeoutError:
                attempt += 1
                delay = 2 ** attempt + random.uniform(0, 1)  # Exponential backoff with jitter
                if attempt < self.max_retries:
                    logging.warning(f"Read timeout for {url}, retrying ({attempt}/{self.max_retries}), next attempt in {delay:.2f} seconds")
                    await asyncio.sleep(delay)
                else:
                    logging.error(f"Read timeout for {url} after {self.max_retries} retries")
            except aiohttp.ClientError as e:
                logging.error(f"Error checking {url}: {e}")
                return
            except asyncio.CancelledError:
                logging.info(f"Task cancelled for {url}")
                return

    async def process_batch(self, paths):
        semaphore = asyncio.Semaphore(self.max_concurrent_requests)
        async with aiohttp.ClientSession() as session:
            tasks = []
            for path in paths:
                url = f"{self.base_url}/{quote_plus(path)}"
                async with semaphore:
                    task = asyncio.create_task(self.fetch(session, url, path))
                    tasks.append(task)

            done, pending = await asyncio.wait(tasks, timeout=None, return_when=asyncio.ALL_COMPLETED)
            for task in pending:
                task.cancel()  # Cancel any pending tasks if exiting
            await asyncio.gather(*tasks, return_exceptions=True)  # Ensure all tasks are handled

    async def search(self):
        start_time = time.time()  # Record start time

        with open(self.wordlist_path, 'r') as f:
            words = f.read().splitlines()
        
        num_words = len(words)
        logging.info(f"Total words in wordlist: {num_words}")

        for i in range(0, num_words, self.batch_size):
            if self.should_exit:
                logging.info("Search interrupted. Outputting found paths...")
                break
            batch_words = words[i:i + self.batch_size]
            paths = self.construct_paths(batch_words)
            logging.info(f"\nProcessing batch {i // self.batch_size + 1}/{(num_words // self.batch_size) + 1}")
            await self.process_batch(paths)

            if self.should_exit:
                logging.info("Search interrupted. Outputting found paths...")
                break

            gc.collect()  # Explicitly collect garbage

        elapsed_time = time.time() - start_time  # Calculate elapsed time
        logging.info(f"Search completed in {elapsed_time:.2f} seconds. Found paths:")
        for path in self.found_paths:
            logging.info(f"{COLOR_GREEN}{path}{COLOR_RESET}")

    def construct_paths(self, words):
        paths = set()
        for word in words:
            paths.add(word)
            for ext in self.extensions:
                paths.add(f"{word}.{ext}")
        return paths

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Asynchronous Directory and File Searcher",
        epilog="Example usage:\npython async_dir_file_searcher.py http://example.com path/to/your/wordlist.txt --extensions html asp php css js json --max_concurrent_requests 20 --batch_size 70"
    )
    parser.add_argument('base_url', type=str, help="The base URL of the website to search (e.g., http://example.com)")
    parser.add_argument('wordlist_path', type=str, help="Path to the wordlist file (e.g., /path/to/wordlist.txt)")
    parser.add_argument('--extensions', type=str, nargs='*', default=['php'], help="File extensions to search for (e.g., --extensions html asp php css js json). Note: .zip is always included)")
    parser.add_argument('--max_concurrent_requests', type=int, default=11, help="Maximum number of concurrent requests (default: 11)")
    parser.add_argument('--max_retries', type=int, default=10, help="Maximum number of retries for failed requests (default: 10)")
    parser.add_argument('--batch_size', type=int, default=40, help="Number of paths to process per batch (default: 40)")

    args = parser.parse_args()

    # Ensure .zip is always included in the extensions
    extensions = list(set(args.extensions + ['zip']))

    searcher = AsyncDirFileSearcher(args.base_url, args.wordlist_path, extensions, args.max_concurrent_requests, args.max_retries, args.batch_size)
    try:
        asyncio.run(searcher.search())
    except KeyboardInterrupt:
        logging.info("Search interrupted by user.")
        # Ensure we exit gracefully without showing traceback
        sys.exit(0)
    except Exception as e:
        logging.error(f"An error occurred: {e}")
        # Ensure we exit gracefully on unexpected errors
        sys.exit(1)
