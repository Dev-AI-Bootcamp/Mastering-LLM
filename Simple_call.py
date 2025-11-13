import os
import sys
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables from .env file
load_dotenv()

# Active: OpenAI GPT5-nano API call
api_key = os.getenv("OPENAI_API_KEY")    
client = OpenAI(api_key=api_key)    
print("Calling OpenAI GPT5-nano...See how long it takes...")

def showStreamedResponse(streamed_response):
    for chunk in streamed_response:
        # Check for the delta content in the first choice
        streamedcontent:str = chunk.choices[0].delta.content
        if streamedcontent:
            print(streamedcontent, end="")
            # Immediately flush the output buffer to ensure real-time printing
            sys.stdout.flush()

messages = [
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "Hello!"},
    {"role": "assistant", "content": "Hi there! How can I help you today?"},
    {"role": "user", "content": "Can you explain recursion in simple terms?"},
    {"role": "assistant", "content": "Sure! Recursion is when a function calls itself to solve smaller parts of a problem."},
    {"role": "user", "content": "Can you give me a Python example?"}
]

response = client.chat.completions.create(
    model="gpt-5-nano",
    messages=messages,
    stream=False
)
print("OpenAI GPT5-nano Response:")
print(response.choices[0].message.content)
#showStreamedResponse(response)


# Google Gemini API call
"""
google_api_key = os.getenv("GEMINI_API_KEY")
google_endpoint ="https://generativelanguage.googleapis.com/v1beta/openai/"
print("Calling Google Gemini STREAMED...See how long it takes...")
GoogleClient = OpenAI(
    api_key=google_api_key,
    base_url=google_endpoint
)
Googleresponse = GoogleClient.chat.completions.create(
    # Use a compatible Gemini model name
    model="gemini-2.5-flash",
    messages=messages,
    stream=True
)
print("Google Gemini Response:")
showStreamedResponse(Googleresponse)
"""




"""
from openai import AzureOpenAI
azure_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")
azure_api_key = os.getenv("AZURE_OPENAI_API_KEY")
azure_deployment = os.getenv("AZURE_OPENAI_DEPLOYMENT")  # Deployment name for GPT5-nano
client = AzureOpenAI(
    azure_endpoint=azure_endpoint,
    api_key=azure_api_key,
    api_version="2024-02-15-preview"  # Use appropriate API version
)
print("Calling Azure OpenAI GPT5-nano...See how long it takes...")
response = client.chat.completions.create(
    model=azure_deployment,  # This is the deployment name in Azure
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Hello! Can you introduce yourself?"}
    ]
)
print("Azure OpenAI GPT5-nano Response:")
print(response.choices[0].message.content)
"""


