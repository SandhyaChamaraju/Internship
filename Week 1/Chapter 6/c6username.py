#Prompt the user to enter a username
username = input("Enter your username: ")

#Check if the length of the username is less than 10 characters
if len(username) < 10:
    print("The username contains less than 10 characters.")
else:
    print("The username contains 10 or more characters.")
