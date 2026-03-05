import asyncio
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

async def main():
    # Connect to your server
    server_params = StdioServerParameters(
        command="python",
        args=["server.py"]
    )

    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()

            # Practice 1 - List all tools
            print("\n--- Available Tools ---")
            tools = await session.list_tools()
            for tool in tools.tools:
                print(f"- {tool.name}: {tool.description}")

            # Practice 2 - Call greet tool
            print("\n--- Calling greet tool ---")
            result = await session.call_tool("greet", {"name": "Segun"})
            print(result.content[0].text)

            # Practice 3 - Read a document
            print("\n--- Reading deposition.md ---")
            result = await session.call_tool(
                "read_doc_contents", 
                {"doc_id": "deposition.md"}
            )
            print(result.content[0].text)
           
            # Practice 4 - Get current time
            print("\n--- Getting current time ---")
            result = await session.call_tool("get_current_time", {})
            print(result.content[0].text)

            # Practice 5 - Edit a document
            print("\n--- Editing deposition.md ---")
            result = await session.call_tool("edit_document", {
                 "doc_id": "deposition.md",
                 "old_str": "Angela Smith",
                 "new_str": "John Doe"
           })
            print(result.content[0].text)
asyncio.run(main())