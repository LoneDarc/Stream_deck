import json
import os


base_setting = {
    "profile_0": { "profile_name" : "default",
        "Buttons": {
            0 : {
                "label" : "default",
                "task_type" : "none",
                "task" : "none"
            },
            1 : {
                "label" : "default",
                "task_type" : "none",
                "task" : "none"
            },
            2 : {
                "label" : "default",
                "task_type" : "none",
                "task" : "none"
            },
            3 : {
                "label" : "default",
                "task_type" : "none",
                "task" : "none"
            },
            4 : {
                "label" : "default",
                "task_type" : "none",
                "task" : "none"
            },
            5 : {
                "label" : "default",
                "task_type" : "none",
                "task" : "none"
            },
            6 : {
                "label" : "default",
                "task_type" : "none",
                "task" : "none"
            },
            7 : {
                "label" : "default",
                "task_type" : "none",
                "task" : "none"
            },
        }
    }
}


def Create_default():
    print("no profiles found, creating now!")
    os.makedirs("save", exist_ok=True)
    file = open("save/profiles.json", "x")

    file.write(json.dumps(base_setting, indent= 2))

    file.close()