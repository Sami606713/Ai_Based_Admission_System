import os
from langchain.agents import initialize_agent, AgentType
from langchain.schema import SystemMessage
from Tools.gather_data_tool import data_gather_tool
from config.model import load_model



def AdmissionAgent(query:str):

    # ========================== #
    #    Define Admission Context
    # ========================== #
    with open("Prompts/system_prompt.md","r",encoding="utf-8") as f:
        ADMISSION_CONTEXT= f.read()


    # ========================== #
    #    Load Tools and Memory
    # ========================== #

    tools, memory = data_gather_tool()

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

    response = admission_agent.run(query)
    return response, memory
# ========================== #
#       Example Interaction
# ========================== #

if __name__ == "__main__":
    query = input("You: ")
    response, memory = AdmissionAgent(query)
    print(response)
    # print(memory)