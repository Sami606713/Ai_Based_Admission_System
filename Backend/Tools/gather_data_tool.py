import os
from langchain.agents import Tool
from langchain.memory import ConversationBufferMemory

def data_gather_tool():
    """Loads the admission prompt and initializes tools for collecting admission information."""
    # Read admission prompt from the file
    with open("Prompts/admission_prompt.md", "r",encoding="utf-8") as f:
        prompt = f.read()

    # ========================== #
    #    Initialize LLM and Memory
    # ========================== #

    # Initialize memory for conversation history
    memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)

    # ========================== #
    #    Define Tools for Agent
    # ========================== #

    def admission_context_tool(query):
        """Return the admission context for reference."""
        return prompt

    tools = [
        Tool(
            name="Admission Context",
            func=admission_context_tool,
            description="Provides context and guidelines for collecting admission information."
        )
    ]

    # Return tools and memory so they can be used by the agent
    return tools, memory

if __name__ == "__main__":
    tools, memory = data_gather_tool()
    print(tools)
    print(memory)