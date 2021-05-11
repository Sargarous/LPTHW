from sys import argv

script, user_name, reason_presense = argv
text = '>>> '

print(f"Hi {user_name}, I'm the {script} script.")
print("I'd like to ask you a few questions.")
print(f"Do you like me, {user_name}?")
likes = input(text)

print(f"Where do you live {user_name}?")
lives = input(text)

print("What kind of computer do you have?")
computer = input(text)

print(f"{user_name}, do you know the reason why u study instead of playing some game or watching some cool anime? {reason_presense}?")


print("Can you name it?")
reason_for_all_of_this = input(text)

print("Can you hold it till the end?")
hold = input(text)

print(f"""
Alright, so you said {likes} about liking me.
You live in {lives}. Not sure where that is.
And you have a {computer} computer. Nice.
So you have a reason and this is {reason_for_all_of_this}. Is up to you to hold on to it. Best of luck.
""")
