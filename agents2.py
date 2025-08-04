from pydantic import BaseModel
from langgraph.prebuilt import create_react_agent
import os
from dotenv import load_dotenv
from langgraph.checkpoint.memory import InMemorySaver
load_dotenv()
from langgraph.prebuilt import create_react_agent




class MailResponse(BaseModel):
   subject: str
   body: str
   regards: str


agent = create_react_agent(
   model="groq:llama-3.3-70b-versatile", 
   tools=[], 
   response_format = MailResponse 
)


config = {"configurable": {"thread_id": "1"}}
response = agent.invoke(
   {"messages": [{"role": "user", "content": "write a mail applying leave for travel"}]},
   config 
)
print(response)
print("------------------------------")
print(response["structured_response"])


print("------------------------------")
print(response["structured_response"].subject)


print("------------------------------")
print(response["structured_response"].body)

print("------------------------------")
print(response["structured_response"].regards)