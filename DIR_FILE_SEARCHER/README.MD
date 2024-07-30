# Asynchronous Directory and File Searcher

## Description

This Python script performs an asynchronous search for directories and files on a given base URL using a wordlist. It supports multiple file extensions and handles requests concurrently to improve performance. It can handle various HTTP status codes and retries requests with exponential backoff in case of timeouts.

## Features

- Asynchronous HTTP requests using `aiohttp`.
- Configurable number of concurrent requests.
- Configurable number of retries with exponential backoff.
- Batch processing of paths to avoid overwhelming the server.
- Signal handling for graceful exit on user interruption.
- Logging with color-coded output for better visibility.

## Requirements

- Python 3.7+
- `aiohttp`
- `asyncio`
- `os`
- `argparse`
- `random`
- `time`
- `signal`
- `sys`
- `logging`
- `urllib`
- `gc`

You can install the required package using pip:

bash
```pip install aiohttp```


## Usage
To use the script, run it from the command line with the following arguments:
```python async_dir_file_searcher.py <base_url> <wordlist_path> [--extensions <ext1> <ext2> ...] [--max_concurrent_requests <number>] [--max_retries <number>] [--batch_size <number>]```

## Example
To search a website with a wordlist and additional file extensions, you could run:
```python async_dir_file_searcher.py http://example.com /path/to/wordlist.txt --extensions html asp php css js json --max_concurrent_requests 20 --batch_size 70
```

## Signal Handling
The script handles SIGINT (Ctrl+C) and SIGTERM signals to ensure a graceful exit. If interrupted, it will stop processing and output the paths it has found up to that point.

## Logging
The script uses the logging module to provide real-time feedback on the search process. Logs include information about found paths, errors, and warnings, with color coding for better visibility.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Author
@Darkstar
