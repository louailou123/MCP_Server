# server.py
from mcp.server.fastmcp import FastMCP
from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()
db_url = os.getenv('DATABASE_URL')

db=MongoClient(db_url)
database=db['School_Management']
collection=database['Students']

# Create an MCP server
mcp = FastMCP("louai") 


# add a student to the students collection tool
@mcp.tool()
def add_student(name: str, skill: str) -> str:
    """Add a student to the students collection"""
    doc = {"name": name, "skill": skill}
    collection.insert_one(doc)
    return ('students inserted')


# Add a dynamic greeting resource
@mcp.resource("greeting://{name}")
def get_greeting(name: str) -> str:
    """Get a personalized greeting"""
    return f"Hello, {name}!"