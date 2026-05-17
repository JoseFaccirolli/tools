from random import random
from math import trunc

digits = 0
while digits < 1 or digits > 5:
    try:
        print("You can only choose a number between 1 and 5")
        digits = int(input("How many digits do you wanna sum (1 - 5): "))
        print()
    except ValueError:
        print("\nYou can only put numbers! And", end=" ")

zero = input("Do you wanna include 0 in the random numbers? (y/N)")
if zero.upper() != "Y" and zero.upper() != "YES":
    print("No zero will be include to the sums")
    zero = False
else:
    print("Zeros possible will be include in to the sums")
    zero = True

while True:
    num1 = trunc(random() * 10 ** digits)
    num2 = trunc(random() * 10 ** digits)
    
    if not zero:
        while num1 == 0:
            num1 = trunc(random() * 10 ** digits)

        while num2 == 0:
            num2 = trunc(random() * 10 ** digits)
    
    Sum = num1 + num2

    try:
        print("---------")
        answer = int(input(f"| {num1} + {num2} = "))

        if answer == Sum:
            print("CORRECT!")
        else:
            print(f"INCORRECT! the sum is: {Sum}")
    except ValueError:
        print(f"INCORRECT! the sum is: {Sum}")
    print()
