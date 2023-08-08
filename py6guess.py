number = 9
guess = int(input("I am thinking of a number btw 0-10, can you guess it?"))

while True:
    if guess == number:
        break
    else:
        guess = int(input("Nope try again"))
print("you guessed it, it was",number)
        
    
