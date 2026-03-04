from mcp.server.fastmcp import FastMCP
from datetime import datetime
import requests
from bs4 import BeautifulSoup

# Create your MCP server
mcp = FastMCP("My First Server")

# Tool 1 - Greet
@mcp.tool()
def greet(name: str) -> str:
    """Greets a person by name"""
    return f"Hello, {name}! MCP is working!"

# Tool 2 - Date and Time
@mcp.tool()
def get_current_time() -> str:
    """Returns the current date and time"""
    now = datetime.now()
    return f"Current date and time is: {now.strftime('%A, %B %d %Y at %H:%M:%S')}"

# Tool 3 - Web Scraper
@mcp.tool()
def scrape_url(url: str) -> str:
    """Scrapes and returns the main text content from any URL"""
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers, timeout=10)
    soup = BeautifulSoup(response.text, "html.parser")
    for tag in soup(["script", "style", "nav", "footer"]):
        tag.decompose()
    text = soup.get_text(separator="\n", strip=True)
    return text[:3000]

# Run the server
if __name__ == "__main__":
    mcp.run()