fav_languages = {}
print("Please enter the names and favorite languages of 4 friends:")

for i in range(4):
    name = input(f"\nEnter the name of friend {i+1}: ")
    
    language = input(f"Enter {name}'s favorite language: ")
    
    fav_languages[name] = language


print("\nFinal Dictionary:")
print(fav_languages)


#Question 7
'''since dictionary keys must be unique,the second friend's language overwrite the first friend's language'''


#Question 8
'''Nothing happens to the program.Dictionary values can be repeated'''
