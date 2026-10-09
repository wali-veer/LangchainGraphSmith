from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain.tools import tool
from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI
from langchain_tavily import TavilySearch

load_dotenv()

llm = ChatOpenAI(model="gpt-4o", temperature=0.5, max_tokens=500)
tools = [TavilySearch()]
agent = create_agent(model=llm, tools=tools)

def main():
    print("Hello from langchaingraphsmith!")
    result = agent.invoke({"messages": HumanMessage(content="Tell me the cricket match score of India vs any 2 countries in the last 3 weeks.")})
    print(f"Agent response: {result}")

if __name__ == "__main__":
    main()