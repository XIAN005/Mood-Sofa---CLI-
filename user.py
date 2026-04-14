import os
import json
from utils import clear_screen
#define the function to ask the user his name
def get_user_name():
    file_path = "data/user.json"

    if os.path.exists(file_path):
        # read the name from the file
        with open(file_path, "r") as f:
            data = json.load(f)
        return data["name"]

    else:
        # first launch : ask the name and save.
        name = input("What is your name?: ")
        clear_screen()
        data = {"name": name}
        with open(file_path, "w") as f:
            json.dump(data, f)
        return name
