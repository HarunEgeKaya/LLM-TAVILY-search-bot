from dotenv import load_dotenv
import os
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_community.tools.tavily_search import TavilySearchResults
from langchain_core.messages import HumanMessage
from langgraph.prebuilt import create_react_agent
from langchain_core.pydantic_v1 import BaseModel

load_dotenv()

search = TavilySearchResults(max_results=2)

tools = [search]

api_key = os.getenv("GEMINI_API_KEY")

model = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash",
    temperature=0.7,
    google_api_key=api_key
)

agent_executor = create_react_agent(model, tools)

if __name__ == "__main__":
    soru = agent_executor.invoke(
        {"messages": [HumanMessage(content="What is the weather in İstanbul today?")]},
    )
    print(soru["messages"][-1].content)