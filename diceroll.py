import random

name = input("What is your name? ")
try:
    dRollAmt = input("How many dice would you like to roll? ")
    dRollAmt = int(dRollAmt)
    dSidesAmt = input("How many sides should each of these dice have? ")
    dSidesAmt = int(dSidesAmt) 
    if (dRollAmt > 0) and (dSidesAmt > 1):
        print("Okay " + name + ", here are the results of your dice rolls:")
        while (dRollAmt > 0):
            dRollAmt -= 1
            randInt = random.randint(1, dSidesAmt)
            print(randInt, end=" ")
    else:
        print("Please enter a valid amount of dice and side amounts.")
except:
    print("Please enter a number next time.")
