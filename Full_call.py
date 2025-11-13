"""
LLM Caller Application
This application demonstrates how to call different LLM APIs:
1. OpenAI GPT5-nano using the standard OpenAI library
2. Google Gemini using the gemini library (commented)
3. OpenAI GPT5-nano via Azure AI Foundry (commented)
"""

import os
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables from .env file
load_dotenv()


def call_openai_gpt5_nano():
    """Call OpenAI's GPT5-nano model using the standard OpenAI library."""
    # Get API key from environment variable
    api_key = os.getenv("OPENAI_API_KEY")
    
    if not api_key:
        print("Error: OPENAI_API_KEY not found in .env file")
        return
    
    # Initialize OpenAI client
    client = OpenAI(api_key=api_key)
    
    try:
        # Create a chat completion request
        print("Calling OpenAI GPT5-nano...See how long it takes...")
        response = client.chat.completions.create(
            model="gpt-5-nano",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": "Hello! Can you introduce yourself?"}
            ],
            max_tokens=150
        )
        
        # Print the response
        print("OpenAI GPT5-nano Response:")
        print(response.choices[0].message.content)
        print(f"\nTokens used: {response.usage.total_tokens}")
        
    except Exception as e:
        print(f"Error calling OpenAI API: {e}")


# Google Gemini API call
def call_google_gemini():
    '''Call Google Gemini using the gemini library.'''
    import google.generativeai as genai
    
    # Get API key from environment variable
    api_key = os.getenv("GEMINI_API_KEY")
    
    if not api_key:
        print("Error: GEMINI_API_KEY not found in .env file")
        return
    
    # Configure the Gemini API
    genai.configure(api_key=api_key)
    
    try:
        
        # Initialize the model
        model = genai.GenerativeModel('gemini-pro')
        
        # Generate content
        print("Calling Google Gemini...See how long it takes...")
        response = model.generate_content("Hello! Can you introduce yourself?")
        
        # Print the response
        print("Google Gemini Response:")
        print(response.text)
        
    except Exception as e:
        print(f"Error calling Google Gemini API: {e}")


# COMMENTED: Azure OpenAI API call
def call_azure_openai_gpt5_nano():
    '''Call OpenAI's GPT5-nano model via Azure AI Foundry.'''
    from openai import AzureOpenAI
    
    # Get Azure credentials from environment variables
    azure_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")
    azure_api_key = os.getenv("AZURE_OPENAI_API_KEY")
    azure_deployment = os.getenv("AZURE_OPENAI_DEPLOYMENT")  # Deployment name for GPT5-nano
    
    if not all([azure_endpoint, azure_api_key, azure_deployment]):
        print("Error: Azure OpenAI credentials not found in .env file")
        print("Required: AZURE_OPENAI_ENDPOINT, AZURE_OPENAI_API_KEY, AZURE_OPENAI_DEPLOYMENT")
        return
    
    
    # Initialize Azure OpenAI client
    client = AzureOpenAI(
        azure_endpoint=azure_endpoint,
        api_key=azure_api_key,
        api_version="2024-02-15-preview"  # Use appropriate API version
    )
    
    try:
        # Create a chat completion request
        print("Calling Azure OpenAI GPT5-nano...See how long it takes...")
        response = client.chat.completions.create(
            model=azure_deployment,  # This is the deployment name in Azure
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": "Hello! Can you introduce yourself?"}
            ],
            max_tokens=150
        )
        
        # Print the response
        print("Azure OpenAI GPT5-nano Response:")
        print(response.choices[0].message.content)
        print(f"\nTokens used: {response.usage.total_tokens}")
        
    except Exception as e:
        print(f"Error calling Azure OpenAI API: {e}")



def main():
    """Main function to demonstrate LLM API calls."""
    print("=" * 60)
    print("LLM Caller Application")
    print("=" * 60)
    print()
    
    # Call OpenAI GPT5-nano (active)
    call_openai_gpt5_nano()
    
    # Call Google Gemini
    call_google_gemini()
    
    # Uncomment the following to call Azure OpenAI
    call_azure_openai_gpt5_nano()


if __name__ == "__main__":
    main()
