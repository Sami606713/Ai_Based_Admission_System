import requests
from dotenv import load_dotenv
from langchain.agents import Tool
import os

load_dotenv()
def upload_data(data):
    """
    This tools is only responsible for uploadind data to the Airtable database.
    input: data (dict) - The data to be uploaded to the database.
    """
    try:
        baseId = os.getenv("baseId")
        tableIdOrName = os.getenv("tableIdOrName")
        authToken = os.getenv("authToken")
        url = f"https://api.airtable.com/v0/{baseId}/{tableIdOrName}"

        # Headers for the request
        headers = {
            "Authorization": f"Bearer {authToken}",
            "Content-Type": "application/json"
        }

         # Convert data into Airtable format
        payload = {
            "records": [{"fields": data}]
        }

        # Make the POST request to Airtable
        response = requests.post(url, headers=headers, json=payload)
        # Check the response status code
        if response.status_code == 200:
            print("Record inserted successfully!")
            print("Response:", response.json())
        else:
            print(f"Error: {response.status_code}")
            print("Response:", response.json())
    except Exception as e:
        return f"Error uploading data: {str(e)}"

if __name__ == "__main__":
   data = {
        "fields": {
            "Name": "name",
            "Previouse_Institute": "previous_institute",
            "Marks": 722,
            "Grade": "grade",
            "Email": "user@example.com",
            "P/Nbr": "1234567890",
            "Program": "AI",
            "CNIC":"1330260368367"
        }
    }
   
   upload_data(data)