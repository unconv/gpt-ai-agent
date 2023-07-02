import openai
import json
import sys
import os

import gpt_functions

openai.api_key = os.getenv("OPENAI_API_KEY")

def parse_function_response(message):
    function_call = message["function_call"]
    function_name = function_call["name"]

    print("GPT: Called function " + function_name )

    try:
        arguments = json.loads(function_call["arguments"])

        if hasattr(gpt_functions, function_name):
            function_response = getattr(gpt_functions, function_name)(**arguments)
        else:
            function_response = "ERROR: Called unknown function"
    except:
        function_response = "ERROR: Invalid arguments"

    return (function_name, function_response)


def run_conversation(message, messages = []):
    messages.append(message)

    with open("messages.json", "w") as f:
        f.write(json.dumps(messages, indent=4))

    response = openai.ChatCompletion.create(
        messages=messages,
        model="gpt-3.5-turbo-0613",
        functions=gpt_functions.definitions,
        function_call="auto",
    )

    message = response["choices"][0]["message"]
    messages.append(message)

    if "function_call" in message:
        function_name, function_response = parse_function_response(message)

        message = {
            "role": "function",
            "name": function_name,
            "content": function_response
        }
    else:
        user_message = input("GPT: " + message["content"] + "\nYou: ")
        message = {
            "role": "user",
            "content": user_message
        }

    run_conversation(message, messages)

messages = [
    {
        "role": "system",
        "content": "You are an AI bot that can do everything using function calls. When you are asked to do something, use the function call you have available and then respond with a message confirming what you have done."
    }
]

user_message = input("GPT: What do you want to do?\nYou: ")
message = {
    "role": "user",
    "content": user_message
}

run_conversation(message, messages)
