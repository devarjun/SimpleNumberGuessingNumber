import random as rd
x = rd.randint(1,100)
ChanceCount = 1
chances = 7
print(f"You've got {chances} chances to guess the number")
while ChanceCount <= 7:
    userInput = int(input("Enter a number to guess\t"))
    chances = chances-1
    if (x == userInput):
        print("you've sucessfully selected")
        break
    else:
        print(f"You are wrong!, you got only {chances}, left")
    ChanceCount  = ChanceCount  + 1
print(f"You've not found it, the actual number is {x}")