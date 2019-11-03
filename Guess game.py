print("\n\t Welcome to the Gusess Game\n\n\t You have only three atemps")
import random
for i in range(3):
    ran=random.randint(1,6)
    number=int(input("enter number > "))
    if number==ran:
        print("you Guess the number.. Congrats ")
        break
    else:
        print("bad luck")


