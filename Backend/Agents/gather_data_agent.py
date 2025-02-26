import os
from langchain.agents import initialize_agent, AgentType
from langchain.schema import SystemMessage
from Tools.gather_data_tool import data_gather_tool
from Tools.data_upload_tool import upload_data
from config.model import admission_model
from langchain.agents import Tool

# ========================== #
#    Load Tools and Memory
# ========================== #
info_gather_tool, memory = data_gather_tool()


# ========================== #
data_upload_tool =[
        Tool(
            name="Data Upload Tool",
            func=upload_data,
            description="Uploads data to the Airtable database."
        )
    ]
# =========Document upload to Airtable================

# ========================== #
#    Define Admission Context
# ========================== #
with open("Prompts/system_prompt.md", "r", encoding="utf-8") as f:
    ADMISSION_CONTEXT = f.read()

# Add system message only once
if not memory.chat_memory.messages:
    memory.chat_memory.add_message(SystemMessage(content=ADMISSION_CONTEXT))

def AdmissionAgent(query: str):
    """
    Initializes and runs the Admission Agent with the provided query.
    """
    try:
        # ========================== #
        #    Initialize Admission Agent
        # ========================== #
        admission_agent = initialize_agent(
            tools=[*info_gather_tool,*data_upload_tool],
            llm=admission_model(),
            agent=AgentType.CONVERSATIONAL_REACT_DESCRIPTION,
            verbose=True,
            memory=memory,
            handle_parsing_errors=True
        )

        # ========================== #
        #       Generate Response
        # ========================== #
        response = admission_agent.run(query)
        return response

    except Exception as e:
        return f"Error processing query: {str(e)}"

# ========================== #
#       Example Interaction
# ========================== #
if __name__ == "__main__":
    while True:
        query = input("You: ")
        if query.lower() == "q":
            break
        response = AdmissionAgent(query)
        print(response)