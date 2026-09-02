import json
import os
from createdefault import Create_default

def display_profile(profile):
    print("profile: " + profile["profile_0"]["profile_name"])
    print("--------------------")
    print("Buttons: ")

    for x in range(0,8):
        print(x+1 , ": Label:     " + profile["profile_0"]["Buttons"][str(x)]["label"] )
        print("    task_type: " + profile["profile_0"]["Buttons"][str(x)]["task_type"])
        print("    task:      " + profile["profile_0"]["Buttons"][str(x)]["task"])



print("Welcome to the stream deck editor\n\n")

print("here you will be able to change what the buttons do on the stream deck\n\n")

try:
    file = open("save/profiles.json", "r")
except FileNotFoundError:
    Create_default()
    file = open("save/profiles.json", "r")

while True:
    print("what would you like to do?\n")
    print("a: edit a profile")
    print("b: display a profile")
    
    inp = input("type a letter")

    os.system('cls' if os.name == 'nt' else 'clear')

    if inp == "a":
        print("you chose a\n\n")
    elif inp == "b":
        display_profile(json.load(file))
    else:
        print("that was not an option\n\n")



file.close()

