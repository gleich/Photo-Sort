import json

with open("supported_file_types.json") as json_file:
    contents = json.load(json_file)
    print(contents)
