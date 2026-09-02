import json
import os

def display_profile(profile):
    print("profile: " + profile["profile_0"]["profile_name"])
    print("--------------------")
    print("Buttons: ")

    for x in range(0,8):
        print(x , ": Label:     " + profile["profile_0"]["Buttons"][str(x)]["label"] )
        print("    task_type: " + profile["profile_0"]["Buttons"][str(x)]["task_type"])
        print("    task:      " + profile["profile_0"]["Buttons"][str(x)]["task"])

base_setting = {
    "profile_0": { "profile_name" : "default",
        "Buttons": {
            0 : {
                "label" : "",
                "task_type" : "",
                "task" : ""
            },
            1 : {
                "label" : "",
                "task_type" : "",
                "task" : ""
            },
            2 : {
                "label" : "",
                "task_type" : "",
                "task" : ""
            },
            3 : {
                "label" : "",
                "task_type" : "",
                "task" : ""
            },
            4 : {
                "label" : "",
                "task_type" : "",
                "task" : ""
            },
            5 : {
                "label" : "",
                "task_type" : "",
                "task" : ""
            },
            6 : {
                "label" : "",
                "task_type" : "",
                "task" : ""
            },
            7 : {
                "label" : "",
                "task_type" : "",
                "task" : ""
            },
        }
    }
}


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



