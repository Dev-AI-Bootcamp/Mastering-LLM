# Mastering-LLM
In this Repo we will be mastering the LLM Calling

## LLM Caller Application

A Python application demonstrating how to call different LLM APIs using UV package manager.

### Features

- **OpenAI GPT5-nano**: Active implementation using the standard OpenAI library
- **Google Gemini**: Commented implementation using the Google Generative AI library
- **Azure OpenAI GPT5-nano**: Commented implementation using Azure AI Foundry

### Prerequisites

- Python 3.12 or higher
- UV package manager

### Installation

1. Clone the repository:
```bash
git clone https://github.com/Dev-AI-Bootcamp/Mastering-LLM.git
cd Mastering-LLM
```

2. The project uses UV for dependency management. Dependencies are already configured in `pyproject.toml`

3. Create a `.env` file based on `.env.example`:
```bash
cp .env.example .env
```

4. Add your API keys to the `.env` file:
   - For OpenAI: Add your `OPENAI_API_KEY`
   - For Google Gemini: Uncomment and add your `GEMINI_API_KEY`
   - For Azure OpenAI: Uncomment and add your Azure credentials

### Usage

Run the application using UV:
```bash
uv run main.py
```

### Switching Between Different LLM Providers

#### Using OpenAI (Default)
The application is configured to use OpenAI's GPT5-nano by default. Simply ensure your `OPENAI_API_KEY` is set in the `.env` file.

#### Using Google Gemini
1. Uncomment the Google Gemini function in `main.py`
2. Uncomment the call to `call_google_gemini()` in the `main()` function
3. Add your `GEMINI_API_KEY` to the `.env` file

#### Using Azure OpenAI
1. Uncomment the Azure OpenAI function in `main.py`
2. Uncomment the call to `call_azure_openai_gpt5_nano()` in the `main()` function
3. Add your Azure credentials to the `.env` file:
   - `AZURE_OPENAI_ENDPOINT`
   - `AZURE_OPENAI_API_KEY`
   - `AZURE_OPENAI_DEPLOYMENT`

### Project Structure

```
.
├── main.py              # Main application file with LLM API calls
├── pyproject.toml       # UV project configuration and dependencies
├── uv.lock             # UV lock file for reproducible builds
├── .env.example        # Example environment variables file
├── .env                # Your actual environment variables (git-ignored)
└── README.md           # This file
```

### Dependencies

- `openai>=2.7.2` - OpenAI API client (also used for Azure OpenAI)
- `google-generativeai>=0.8.5` - Google Generative AI library for Gemini
- `python-dotenv>=1.2.1` - Load environment variables from .env file

### Getting API Keys

- **OpenAI**: https://platform.openai.com/api-keys
- **Google Gemini**: https://aistudio.google.com/app/apikey
- **Azure OpenAI**: Create a resource in Azure Portal and get credentials from there

### License

See LICENSE file for details.
