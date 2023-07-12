#!/usr/bin/env python3

import openai
import json
import sys
import os

import gpt_functions

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


def flip_roles(messages):
    for message in messages:
        if message["role"] == "user":
            message["role"] = "assistant"
        elif message["role"] == "assistant":
            message["role"] = "user"
    return messages


def run_conversation(message, system_messages, messages = [{}], system_number = 0):
    system_data = system_messages[system_number]

    system_message = {
        "role": "system",
        "content": f"{system_data['description']}. Always start your message with your name: '{system_data['name']}' and a colon."
    }

    messages[0] = system_message
    if len(messages) % 5 == 0:
        messages.append(system_message)

    system_number += 1
    if system_number > len(system_messages)-1:
        system_number = 0

    if message:
        messages.append(message)
        print("\n" + message["content"])

    with open("messages.json", "w") as f:
        f.write(json.dumps(messages, indent=4))

    response = openai.ChatCompletion.create(
        messages=messages,
        model="gpt-4-0613",
        functions=gpt_functions.definitions,
        function_call="auto",
    )

    message = response["choices"][0]["message"]

    if "function_call" in message:
        function_name, function_response = parse_function_response(message)

        message = {
            "role": "function",
            "name": function_name,
            "content": function_response
        }
    else:
        messages = flip_roles(messages)

    run_conversation(message, system_messages, messages, system_number)

openai.api_key = os.getenv("OPENAI_API_KEY")

if not openai.api_key:
    openai.api_key = input("Please enter your OpenAI API-key: ")

system_file = input("Please enter system message file from 'system' folder: ")

if not system_file:
    system_file = "php-python-rust.json"

system_file = system_file.removesuffix(".json").removeprefix("system/").removeprefix("system\\")+".json"

with open(os.path.join(os.path.dirname(__file__), "system", system_file), "r") as f:
    system_messages = json.load(f)

run_conversation(None, system_messages)
