#main functions for the chatbot
import openai
import os


def authenticate(str:API_KEY):
    os.environ["API_KEY"] = API_KEY
    openai.api_key = os.getenv("API_KEY")
    if openai.api_key:
        return 1
    else:
        return 0        

