Start the working directory :

uv init mcp-server-demo
cd mcp-server-demo

Then add MCP to your project dependencies:

uv add "mcp[cli]"


To run the mcp command with uv:

uv run mcp

You can install this server in Claude Desktop and interact with it right away by running:


uv run mcp install main.py --with pymongo




