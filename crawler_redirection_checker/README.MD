# URL Redirection and Crawling Tool

A Python script to check for URL redirections and crawl web pages. This tool performs redirection checks and recursively crawls pages up to a specified depth, with results saved in either text or Excel formats.

## Features

- **Check for URL Redirections:** Resolve final destination URLs from initial URLs.
- **Web Crawling:** Recursively crawl pages up to a specified depth to discover additional links.
- **Result Saving:** Save results in either text or Excel formats.
- **User-Agent Rotation:** Mimic different clients to avoid being blocked.

## Requirements

- Python 3.7 or higher
- Required Python packages: `requests`, `beautifulsoup4`, `lxml`, `openpyxl`, `aiohttp`

Install the required packages using `pip`:

```
pip install requests beautifulsoup4 lxml openpyxl aiohttp 
```

## Usage
### Command-Line Interface
You can run the script from the command line with various options.

## Check a Single URL
To check redirection for a single URL:
```
python script.py -u http://example.com
```

### Check a Single URL and Save Results
To check redirection for a single URL and save results in an Excel file:
```
python script.py -u http://example.com -o results.xlsx -fmt xlsx
```

### Process URLs from a File
To check redirections for multiple URLs listed in a file:
```
python script.py -f urls.txt
```

### Process URLs from a File and Save Results
To check redirections for multiple URLs from a file and save results in a text file:
```
python script.py -f urls.txt -o results.txt -fmt txt
```

### Specify Crawling Depth
To specify the maximum depth for crawling:
```
python script.py -u http://example.com -d 3
```

Arguments
```
-u, --url : URL to check for redirections.
-f, --file : Path to a file containing URLs to check for redirections.
-o, --output : Path to the output file where results will be saved.
-fmt, --format : Format for the output file (txt or xlsx).
-d, --depth : Maximum depth for crawling (default: 4).
```

### Example Usage
Check a single URL with default settings:
```
python script.py -u http://example.com
```

Check a single URL and save results to an Excel file:
```
python script.py -u http://example.com -o results.xlsx -fmt xlsx
```

Process URLs from a file and save results in text format:
```
python script.py -f urls.txt -o results.txt -fmt txt
```

## Contributing
Contributions are welcome! Please fork the repository and submit a pull request with your changes. Ensure that your code adheres to the existing style and includes relevant tests.


## Contact
For any questions or issues, please open an issue on the GitHub repository or contact @Darkstar.
