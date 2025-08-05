from dotenv import load_dotenv
load_dotenv()
import asyncio
from langchain_mcp_adapters.client import MultiServerMCPClient
from langgraph.prebuilt import create_react_agent
import os

GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")

async def run_agent():
   client = MultiServerMCPClient(
       {
           "github": {
               "command": "npx",
               "args": [
                   "-y",
                   "@modelcontextprotocol/server-github"
               ],
               "env": {
                   "GITHUB_PERSONAL_ACCESS_TOKEN": GITHUB_TOKEN
               },
               "transport": "stdio"
           },
           "filesystem": {
               "command": "npx",
               "args": [
                   "-y",
                   "@modelcontextprotocol/server-filesystem",
                   "/Users/spu/venv"
               ],
               "transport":"stdio"
           }
       }
   )

   tools = await client.get_tools()
   print("------")
   print(tools)
   print("------")
   agent = create_react_agent("grok:llama-3.1-8b-instant", tools)

   print("------")
   response = await agent.ainvoke({"messages": "what are the files present in /Users/spu/venv/"})
   print(response["messages"][-1].content)
   print("------")

   #print(response["messages"][-1].content)

if __name__ == "__main__":
   asyncio.run(run_agent())





