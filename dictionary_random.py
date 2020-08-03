import random

random_choices = {
    "message1": "There is only one way to success, it's called hard work! Keep it up! ",
    "message2": "Sometimes the best thing to do is sleep!",
    "message3": "Limits only exist in your mind!",
    "message4": "The capacity to learn is a gift, the ability to learn is a skill!",
    "message5": "Every accomplishment starts with the decision to try!"
}

random_selection = random_choices[f"message{str(random.randint(1,5))}"]

user_input = {
    "name": "",
    "mood": "",
}

user_input["name"] = input("Please enter your name: ")
user_input["mood"] = input("How are you today: ")

print("Welcome %s, let this message guide your mood today: " % (user_input["name"]))

print(random_selection)

another_message = input("Would you like another message? ('Yes' or 'No'): ")
print_another_message = 'Yes'

while print_another_message == 'Yes':
    random_selection = random_choices[f"message{str(random.randint(1,5))}"]
    print(random_selection)
    print_another_message = input("Another message? ('Yes' or 'No'): ")