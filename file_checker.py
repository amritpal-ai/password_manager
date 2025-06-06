import json
import os

file_name = "user_data.json"

# This function loads data from the file or creates it if it doesn't exist
def load_data():
    if not os.path.exists(file_name):
        with open(file_name, "w") as file:
            json.dump({}, file)

    with open(file_name, "r") as file:
        data = json.load(file)
    return data

# This function saves data to the file
def save_data(data):
    with open(file_name, "w") as file:
        json.dump(data, file, indent=4)
