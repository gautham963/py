import random
print("This is a color guessing program if u choose the crrct color u win\n")

colors = ['blue','red','green','yellow','violet','purple']

while True:
     
    ra_clr = colors[random.randint(0,len(colors)-1)]
    color = input("choose any color from 'Blue','Red','Green','Yellow','Violet','Purple'\n")

    while True:
        if (ra_clr == color):
            break
        else:
            color = input("Nope, try again!")
            
    print("You hv guessed it!,WOW",ra_clr)

    pl_again = input("Shall we play again, if u want to quit just type 'no'")

    if(pl_again == 'no'):
        break
    
print("Hey it was fun playing, come back again")

    
