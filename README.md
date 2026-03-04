# MCP First Server

A Model Context Protocol (MCP) server built with Python, connecting Claude Desktop to custom tools.

## Tools

- **greet** - Greets a person by name
- **get_current_time** - Returns the current date and time
- **scrape_url** - Scrapes and returns clean text content from any URL

## Setup

1. Clone the repo
2. Create a conda environment: `conda create -n mcp-project python=3.13`
3. Activate it: `conda activate mcp-project`
4. Install dependencies: `pip install mcp requests beautifulsoup4`
5. Run the server: `python server.py`

## Testing

Use the MCP Inspector:
```
pip install 'mcp[cli]'
mcp dev server.py
```

## Built With
- Python 3.13
- MCP Python SDK
- BeautifulSoup4
- Claude Desktop
