import random

p1=input("Enter (Rock/Paper/Scissors):")
L1=["Rock","Paper","Scissors"]
p2=random.choice(L1)
print("Player 1: ",p1)
print("Player 2: ",p2)

if(p1 == p2):
    print("It's a tie!!")
else:
    if(p1=="Rock"):
        if(p2 == "Paper"):
            print("Player 2 Wins!!")
        elif(p2== " Scissors"):
            print("Player 1 Wins!!")
    elif(p1=="Paper"):
        if(p2 == "Rock"):
            print("Player 1 Wins!!")
        elif(p2== " Scissors"):
            print("Player 2 Wins!!")
    elif(p1=="Scissors"):
        if(p2 == "Rock"):
            print("Player 2 Wins!!")
        elif(p2== " Paper"):
            print("Player 1 Wins!!")

# Enter (Rock/Paper/Scissors):Paper
# Player 1:  Paper
# Player 2:  Rock
# Player 1 Wins!!
