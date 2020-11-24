#This program greets the world and asks the user
#how they are doing.

print("Hello world")
userFeeling = input("Are doing well? Y/N: ")
if userFeeling == "Y":
    print("I am glad that you are doing well.")
elif userFeeling == "N":
    print("That is too bad. I hope things get better for you soon!")
else:
    while userFeeling != "Y" or userFeeling != "N":
        userFeeling = input("I am not sure how you feel. Are you doing well? Y/N ")
        if userFeeling == "Y":
            print("I am glad that you are doing well.")
            break
        elif userFeeling == "N":
            print("That is too bad. I hope things get better for you soon!")
            break
