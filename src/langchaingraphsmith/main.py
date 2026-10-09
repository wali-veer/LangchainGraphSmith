from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain.tools import tool
from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI
from tavily import TavilyClient

load_dotenv()

tavily = TavilyClient()

@tool
def search(query: str) -> str:
    """
    Tool that searches over the Internet
    Args:
        query: The search query to look up
    Returns:
        A string containing the search results
    """
    print(f"Searching for: {query}")
    return tavily.search(query=query)

llm = ChatOpenAI(model="gpt-4o", temperature=0.5, max_tokens=500)
tools = [search]
agent = create_agent(model=llm, tools=tools)

def main():
    print("Hello from langchaingraphsmith!")
    result = agent.invoke({"messages": HumanMessage(content="Search for 3 individual job openings listed based on their posting date, in the field of SRE at leadership level on various job portals.")})
    print(f"Agent response: {result}")

if __name__ == "__main__":
    main()