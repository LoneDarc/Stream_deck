import json
import os

def display_profile(profile):
    print(profile)

base_setting = {
    "Button": 0,
    "Task_type": "None",
    "Task": "None"}


print("Welcome to the stream deck editor\n\n")

print("here you will be able to change what the buttons do on the stream deck\n\n")

try:
    file = open("save/profiles.json", "r")
    display_profile(json.load(file))
except FileNotFoundError:
    print("no profiles found, creating now!")
    os.makedirs("save", exist_ok=True)
    file = open("save/profiles.json", "x")

    file.write(json.dumps(base_setting))

    file.close()



