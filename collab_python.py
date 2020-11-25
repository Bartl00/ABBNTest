#This program is meant to explain the relationships
#between user-entered integers

#Declaring control loop variable
continueProgram = "Y"

#begin loop
while continueProgram != "N":
    #Prompt the user to enter two integers or the sentinel value to end
    #the program
    print("Enter two integers and I will tell you the relationships they satisfy.")
    firstInteger = int(input("Enter the first integer: "))
    secondInteger = int(input("Enter the second integer: "))

    #Compare the two integers using if-statements
    #and print the resulting relationships.
    if firstInteger > secondInteger:
        if firstInteger == secondInteger:
            print(firstInteger, "is equal to ", secondInteger)
            print(firstInteger, "is not less than ", secondInteger)
            print(firstInteger, "is less than or equal to ", secondInteger)
        else:
            print(firstInteger, "is not equal to ", secondInteger)
            print(firstInteger, "is not less than ", secondInteger)
            print(firstInteger, "is not less than or equal to ", secondInteger)
    else:
        firstInteger < secondInteger
        if firstInteger == secondInteger:
            print(firstInteger, "is equal to ", secondInteger)
            print(firstInteger, "is not less than ", secondInteger)
            print(firstInteger, "is less than or equal to ", secondInteger)
        else:
            print(firstInteger, "is not equal to ", secondInteger)
            print(firstInteger, "is less than ", secondInteger)
            print(firstInteger, "is less than or equal to ", secondInteger)
    #Ask the user to loop the program or end it
    continueProgram = input("Do you want to enter two more numbers? \nEnter Y or N: ")
