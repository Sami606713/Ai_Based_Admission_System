# agents.py

import os
from langchain.agents import initialize_agent, AgentType
from langchain.schema import SystemMessage
from Tools.gather_data_tool import data_gather_tool
from config.model import load_model

# ========================== #
#    Load Tools and Memory
# ========================== #
tools, memory = data_gather_tool()

def AdmissionAgent(query: str, memory):
    """
    Initializes and runs the Admission Agent with the provided query and memory.
    """
    # ========================== #
    #    Define Admission Context
    # ========================== #
    with open("Prompts/system_prompt.md", "r", encoding="utf-8") as f:
        ADMISSION_CONTEXT = f.read()

    # Add system message to memory if needed
    memory.chat_memory.add_message(SystemMessage(content=ADMISSION_CONTEXT))

    # ========================== #
    #    Initialize Admission Agent
    # ========================== #
    admission_agent = initialize_agent(
        tools=tools,
        llm=load_model(),
        agent=AgentType.CONVERSATIONAL_REACT_DESCRIPTION,
        verbose=True,
        memory=memory,
        handle_parsing_errors=True
    )

    # ========================== #
    #       Generate Response
    # ========================== #
    response = admission_agent.run(query)
    return response, memory


# ========================== #
#       Example Interaction
# ========================== #
if __name__ == "__main__":
    while True:
        query = input("You: ")
        if query.lower() == "q":
            break
        response, memory = AdmissionAgent(query, memory)
        print(response)
    # print(memory)  # Uncomment to inspect memory if needed