'''
Create a program that prompts the user to input their name once.
Then, the program repeatedly prints out
the name with the first letter capitalized.
'''
while True:

    user_name = input("Enter your name: ")

    capitalized_name = user_name.capitalize()

    print(capitalized_name)
