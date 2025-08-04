from langgraph.prebuilt import create_react_agent
import os
from dotenv import load_dotenv
from langgraph.checkpoint.memory import InMemorySaver

checkpointer = InMemorySaver()

load_dotenv()

def get_weather(city: str) -> str:  
    """Get weather for a given city."""
    return f"It's always sunny in {city}!"

agent = create_react_agent(
    model="groq:llama-3.1-8b-instant",  
    tools=[get_weather],  
    prompt="You are a helpful assistant",  
    checkpointer=checkpointer
)

# Run the agent
config = {"configurable": {"thread_id": "1"}}
res = agent.invoke(
    {"messages": [{"role": "user", "content": "who is modi"}]},
    {"configurable": {"thread_id": "1"}}
)
#print(res)

print(res["messages"][-1].content)

# Run the agent
res = agent.invoke(
    {"messages": [{"role": "user", "content": "when was he born"}]},
    {"configurable": {"thread_id": "2"}}
)
#print(res)

print(res["messages"][-1].content)

try:
   img = agent.get_graph().draw_mermaid_png()
   with open("agent.png", "wb") as f:
       f.write(img)
except Exception:
   pass