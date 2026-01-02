# AI chatbot 🤖

## Overview

This is a simple AI chatbot powered by the Ollama server and the `gemma2:9b` model. The bot is designed to have a friendly personality, loves football (especially FC Barcelona), and enjoys helping with programming problems (you can change this settings).

## Prerequisites

Before running the chatbot, ensure the following:

1. **Python**: Install Python 3.7 or higher.
2. **Python Package**: Install the `openai` Python package:
   ```bash
        pip install openai
   ```
3. **Ollama Server**: Ensure the Ollama server is installed and running locally on `http://localhost:11434`. You can download Ollama from its official website.

## How to Run the Bot Locally

Follow these steps to run the chatbot:

1. Clone this repository or download the project files.
2. Open a terminal and navigate to the project directory:
    ```bash
        cd AI_chatbot
    ```
3. Run the chatbot script:
    ```bash
        python ai_bot.py
    ```
4. Interact with the bot by typing your messages. To exit the chat, type `exit`.

## Features

- **Predefined Personality**: The bot is pre-configured with a friendly personality. You can modify yourself by changing the prompt in `BEST_MODEL`.
- **Streaming Responses**: The bot streams its responses in real-time for a conversational experience.

## Note

- **Model**: The bot uses the `gemma2:2b` model by default. Ensure this model is available in your Ollama server. You can check available models using `ollama list`.
- **Memory Requirements**: The `gemma2:2b` model requires at least 1.6 GB of system memory. Ensure your system meets this requirement.
- **No API Key Needed**: When using Ollama locally, no API key is required.

## License

This project is created for educational purpose.
