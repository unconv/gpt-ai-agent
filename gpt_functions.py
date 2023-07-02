import json

def write_file(filename, content):
    sure = input("Do you want to write to " + filename + "? (YES/NO) ")
    if sure == "YES":
        with open(filename, "w") as f:
            f.write(content)
        return "Successfully written file " + filename
    else:
        return "ERROR: You are not allowed to write to this file"

def get_jokes(number_of_jokes):
    return json.dumps(["Why don't scientists trust atoms? Because they make up all the things!", 'How did the computer get wasted? It took screenshots!', "Why don't skeletons fight other skeletons? They don't have the guts!"])

definitions = [
    {
        "name": "get_jokes",
        "description": "Gets jokes from the joke database",
        "parameters": {
            "type": "object",
            "properties": {
                "number_of_jokes": {
                    "type": "number",
                    "description": "Gets the specified number of jokes"
                }
            }
        },
        "required": ["number_of_jokes"]
    },
    {
        "name": "write_file",
        "description": "Writes content to a file",
        "parameters": {
            "type": "object",
            "properties": {
                "filename": {
                    "type": "string",
                    "description": "Filename to write to"
                },
                "content": {
                    "type": "string",
                    "description": "Content to write to file"
                }
            }
        },
        "required": ["filename", "content"]
    }
]
