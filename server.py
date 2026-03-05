from mcp.server.fastmcp import FastMCP
from datetime import datetime
from pydantic import Field
import requests
from bs4 import BeautifulSoup

# Create your MCP server
mcp = FastMCP("My First Server")

# Document store
docs = {
    "deposition.md": "This deposition covers the testimony of Angela Smith, P.E.",
    "report.pdf": "The report details the state of a 20m condenser tower.",
    "financials.docx": "These financials outline the project's budget and expenditures.",
    "outlook.pdf": "This document presents the projected future performance of the system.",
    "plan.md": "The plan outlines the steps for the project's implementation.",
    "spec.txt": "These specifications define the technical requirements for the equipment.",
}

# Resources
@mcp.resource(
    "docs://documents",
    mime_type="application/json"
)
def list_docs() -> list[str]:
    return list(docs.keys())

@mcp.resource(
    "docs://documents/{doc_id}",
    mime_type="text/plain"
)
def fetch_doc(doc_id: str) -> str:
    if doc_id not in docs:
        raise ValueError(f"Doc with id {doc_id} not found")
    return docs[doc_id]

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

# Tool 4 - Read Document
@mcp.tool(
    name="read_doc_contents",
    description="Read the contents of a document and return it as a string."
)
def read_document(
    doc_id: str = Field(description="Id of the document to read")
):
    if doc_id not in docs:
        raise ValueError(f"Doc with id {doc_id} not found")
    
    return docs[doc_id]

# Tool 5 - Edit Document
@mcp.tool(
    name="edit_document",
    description="Edit a document by replacing a string in the documents content with a new string."
)
def edit_document(
    doc_id: str = Field(description="Id of the document that will be edited"),
    old_str: str = Field(description="The text to replace. Must match exactly, including whitespace."),
    new_str: str = Field(description="The new text to insert in place of the old text.")
):
    if doc_id not in docs:
        raise ValueError(f"Doc with id {doc_id} not found")
    
    docs[doc_id] = docs[doc_id].replace(old_str, new_str)
    return docs[doc_id]

# Run the server
if __name__ == "__main__":
    mcp.run()