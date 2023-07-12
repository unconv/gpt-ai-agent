import json

def write_file(filename, content):
    sure = input("Do you want to write to " + filename + "? (YES/NO) ")
    if sure == "YES":
        with open(filename, "w") as f:
            f.write(content)
        return "Successfully written file " + filename
    else:
        return "ERROR: You are not allowed to write to this file"

definitions = [
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
