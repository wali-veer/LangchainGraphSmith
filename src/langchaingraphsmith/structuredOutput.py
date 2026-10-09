from typing import List

from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain.tools import tool
from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI
from langchain_tavily import TavilySearch
from pydantic import BaseModel, Field

load_dotenv()

class Source(BaseModel):
    """ Schema for a source used by the agent. """
    url:str = Field(description="The URL of the source")

class ResultOfMatch(BaseModel):
    """ Indicate whether India has won the match or not. HEY!!! means win, NOO!!! means lost """
    resultofmatch:str = Field(description="HEY!!! means india has won, NOO!!! means India has lost")

class AgentResponse(BaseModel):
    """ Schema for the agent's response with an answer and sources. """
    answer: str = Field(description="The answer provided by the agent")
    sources: List[Source] = Field(default_factory=list, description="A list of sources used by the agent to generate the answer")
    resultofmatch: List[ResultOfMatch] = Field(description="The result of the cricket match for India")


llm = ChatOpenAI(model="gpt-4o", temperature=0.5, max_tokens=500)
tools = [TavilySearch()]
agent = create_agent(model=llm, tools=tools, response_format=AgentResponse)

def main():
    print("Hello from langchaingraphsmith!")
    result = agent.invoke({"messages": HumanMessage(content="Tell me the cricket match score of India vs any 2 countries in the last 3 weeks.")})
    print(f"Agent response: {result}")

if __name__ == "__main__":
    main()