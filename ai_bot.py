from openai import OpenAI

client = OpenAI(
    base_url="http://localhost:11434/v1",
    api_key="ollama" # no need for an API key when using Ollama locally
)

BEST_MODEL = """
You are my best bro and you are very helpful.
You call me Minh.
You love football and you are a big fan of FC Barcelona.
You are a very good programmer and you love to help people with their problems.
"""

# Initialize the messages list with a system message to set the context for the conversation
messages = [{"role": "system", "content": BEST_MODEL}]

# Take input from user, if the userr types "exit" then exit the program
while True:
    print(messages)
    user_input = input("You: ")
    if user_input.lower() == "exit":
        break
    
    # Add the user input to the messages list
    messages.append({"role": "user", "content": user_input})

    response = client.chat.completions.create(
        model="gemma2:2b",
        stream=True,
        messages=messages
    )

    bot_reply = ""

    # Print the response as it is generated
    for chunk in response:
        bot_reply += chunk.choices[0].delta.content or ""
        print(chunk.choices[0].delta.content or "", end="", flush=True)

    messages.append({"role": "assistant", "content": bot_reply})
    