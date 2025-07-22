#Tavily bazı sorguları hatalı yapıyor, ve ilk sorgudan sonra bir daha tavily kullanılmıyor nedense.. Bu kodda hafıza yok, yani bir istek isterse sizden aynı yerde tekrarlayabilir.


from dotenv import load_dotenv
import os
from langchain_core import memory
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_community.tools.tavily_search import TavilySearchResults
from langchain_core.messages import HumanMessage, AIMessage
from langgraph.prebuilt import create_react_agent
from langchain_core.pydantic_v1 import BaseModel
from langgraph.checkpoint.sqlite import SqliteSaver
import uuid

load_dotenv()

search = TavilySearchResults(max_results=2)
tools = [search]
memory = SqliteSaver.from_conn_string(":memory:")

api_key = os.getenv("GEMINI_API_KEY")

model = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash",
    temperature=0.7,
    google_api_key=api_key
)

agent_executor = create_react_agent(model, tools, checkpointer=memory)

if __name__ == '__main__':
    while True:
        user_input = input("Please enter your question: ")

        user_id = str(uuid.uuid4())
        thread_id = f"thread_{user_id}"

        config = {"configurable": {"thread_id": thread_id}}

        soru = agent_executor.invoke(
            {"messages": [HumanMessage(content=user_input)]}, config
        )

        if len(soru["messages"]) > 1 and isinstance(soru["messages"][-2], AIMessage):
            tool_message = soru["messages"][-2]
            if isinstance(tool_message, AIMessage):
                print(f"AI Response: {tool_message.content}")

        if isinstance(soru["messages"][-1], AIMessage):
            print(soru["messages"][-1].content)
        else:
            print("Son mesaj AIMessage türünde değil.")

        print("----")
