"""
Function to check the validity of the openai api key
"""

import openai
import os

def authenticate(API_KEY: str) -> bool:   
    client = openai.OpenAI(api_key=API_KEY) 
    try:

        if client.models.list():
        # Making a test request to validate the API key  # This is a simple call to check API key validity
            return True
    except openai.AuthenticationError:
        return False
    except Exception as e:
        print(f"An error occurred: {e}")
        return False
