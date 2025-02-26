import langchain
from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os
load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

def admission_model():
    model =ChatGroq(
        groq_api_key=GROQ_API_KEY,
        model="mistral-saba-24b",
        temperature=0.1,  # Controls randomness (0 = deterministic, 1 = more random)
        max_tokens=8192,  # Limits response length
    )
    return model


def query_router_model():
    model =ChatGroq(groq_api_key=GROQ_API_KEY,model='gemma2-9b-it',temperature=0,
        max_tokens=8192 )
    return model

def conversation_model():
    model =ChatGroq(groq_api_key=GROQ_API_KEY,model='llama-3.3-70b-specdec',temperature=0.1,  # Controls randomness (0 = deterministic, 1 = more random)
        max_tokens=131072 )
    return model

if __name__ == "__main__":
    model = admission_model()
    response = model.invoke("What are agents?")
    print(response)