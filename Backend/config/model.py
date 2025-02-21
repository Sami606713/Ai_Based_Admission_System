import langchain
from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os
load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

def load_model():
    model =ChatGroq(groq_api_key=GROQ_API_KEY)
    return model

if __name__ == "__main__":
    model = load_model()
    response = model.invoke("What are agents?")
    print(response)