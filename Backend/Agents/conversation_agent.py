import os
from langchain_community.tools import TavilySearchResults
from langchain.agents import initialize_agent, AgentType
from langchain.agents import Tool
from Tools.conversation_tool import search_tool
from config.model import load_model



def conversation_agent(query):
    # Define tools for the agent 
    tools = [
        Tool(
            name="Search",
            func=search_tool,  # Custom function returning content and URL
            description="Useful for searching information from the web. Returns content and URL."
        )
    ]

    # Create an agent
    agent = initialize_agent(
        tools=tools,
        llm=load_model(),
        agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        verbose=True,
        handle_parsing_errors=True
    )

    # Example query
    response = agent.run(query)
    return response

if __name__ == "__main__":
    query = "What is the fee structure of the university of Haripur?"
    response = conversation_agent(query)
    print(response)