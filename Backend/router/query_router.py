from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableLambda
from config.model import query_router_model


def route_query(query:str):
    
    # Step 1: Define the prompt template with examples
    intent_creation_prompt = PromptTemplate(
        template="""
        Determine the user's intent based on the query provided. 
        Classify the intent into one of the two categories and return **only the category name as a single word**. 
        Do not include any additional text, explanations, or punctuation.

        ### Categories:
        - **information**: For queries seeking general details about the college, such as courses, faculty, fees, facilities, or campus life.
        - **admission**: For queries related to applying for admission, enrollment procedures, deadlines, or required documents.

        ### Rules:
        1. The output must be a single word: either `information` or `admission`.
        2. Do not include any additional text or explanations.
        3. Focus on accurately identifying the intent even if the query is indirect or conversational.

        ### Examples:
        1. User Query: "What courses do you offer in computer science?"
        Intent: information
        2. User Query: "How do I apply for admission next semester?"
        Intent: admission
        3. User Query: "Can you tell me about the campus facilities?"
        Intent: information
        4. User Query: "What documents are required for enrollment?"
        Intent: admission
        5. User Query: "Do you have dormitories for students?"
        Intent: information
        6. User Query: "Is there a deadline for submitting the application?"
        Intent: admission

        ### User Query:
        {query}

        ### Intent:
        """,
        input_variables=["query"]
    )


 
    # Step 2: Define the intent classification pipeline
    
    intent_chain = intent_creation_prompt | query_router_model() | StrOutputParser()

    intent = intent_chain.invoke(query)
    return intent

if __name__ == "__main__":
    query = "What courses do you offer in computer science?"
    intent = route_query(query)

    print(intent)