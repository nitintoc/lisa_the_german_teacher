"""
Function to check the validity of the openai api key
"""

import openai
import os

def authenticate(API_KEY: str) -> bool:
    os.environ["OPENAI_API_KEY"] = API_KEY
    openai.api_key = os.getenv("OPENAI_API_KEY")
    
    try:
        # Making a test request to validate the API key
        openai.Engine.list()  # This is a simple call to check API key validity
        return True
    except openai.error.AuthenticationError:
        return False
    except Exception as e:
        print(f"An error occurred: {e}")
        return False
