import random

number = random.randint(0,10)

guess = int(input("I was guessing a number, can u guess it: "))

while True:
    if guess == number:
        break
    else:
        guess = int(input("Nope, try again: "))
print(" Yay, you guessed it!")
        
        
