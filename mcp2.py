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
                   "/Users/spu/venv/venv"
               ],
               "transport":"stdio"
           }
       }
   )

   tools = await client.get_tools()

   print("------")
   print(tools)
   print("------")
   agent = create_react_agent("groq:llama-3.1-8b-instant", tools)

#    print("------")
#    response = await agent.ainvoke({"messages": "What are the files present in /Users/spu/venv/venv"})
#    print(response["messages"][-1].content)
#    print("------")


#    print("------")
#    response = await agent.ainvoke({"messages": "add a new file new1.txt in the directory /Users/spu/venv/venv"})
#    print(response["messages"][-1].content)
#    print("------")

   #print(response["messages"][-1].content)

   print("------")
   response = await agent.ainvoke({"messages": "delete the file new1.txt in the directory /Users/spu/venv/venv"})
   print(response["messages"][-1].content)
   print("------")


if __name__ == "__main__":
   asyncio.run(run_agent())








