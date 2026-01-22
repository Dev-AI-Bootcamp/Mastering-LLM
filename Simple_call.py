import os
import sys
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables from .env file
load_dotenv()

# Active: OpenAI GPT5-nano API call
api_key = os.getenv("OPENAI_API_KEY")    
    
client= OpenAI(
    api_key=api_key,
) 
model_name="gpt-5-mini"
print("Calling OpenAI GPT5-nano...See how long it takes...")

# function that shows different OpenAI Types of responses.
def showStreamedResponse(streamed_response):
    choices = getattr(streamed_response, "choices", None)
    if choices is not None:
        print(choices[0].message.content)
    else:
        for chunk in streamed_response:
            streamedcontent:str = chunk.choices[0].delta.content
            if streamedcontent:
                print(streamedcontent, end="")
            sys.stdout.flush()

messages = [
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "Hello!"},
    {"role": "assistant", "content": "Hi there! How can I help you today?"},
    {"role": "user", "content": "Can you explain recursion in simple terms?"},
    {"role": "assistant", "content": "Sure! Recursion is when a function calls itself to solve smaller parts of a problem."},
    {"role": "user", "content": "Tell me a 1000 word story about a programmers and his love of python."}
]


# Calling OpenAI with the OpenAI Python SDK

response = client.chat.completions.create(
    model=model_name,
    messages=messages,
    stream=False
)
print(f"The response from {model_name} is:")
showStreamedResponse(response)



# Want to do it with Google? Let's talk about it!
# google_endpoint ="https://generativelanguage.googleapis.com/v1beta/openai/"

# And on Sunday let's come back here with Microsoft Foundry.

