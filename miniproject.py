import random

num=int(input("Enter the number of times you want to play this game:"))
play1Counter=0
play2Counter=0
for i in range(num):
    print("GAME {}".format(i+1))
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
                play2Counter+=1
            elif(p2 == "Scissors"):
                print("Player 1 Wins!!")
                play1Counter+=1
        elif(p1=="Paper"):
            if(p2 == "Rock"):
                print("Player 1 Wins!!")
                play1Counter+=1
            elif(p2== "Scissors"):
                print("Player 2 Wins!!")
                play2Counter+=1
        elif(p1=="Scissors"):
            if(p2 == "Rock"):
                print("Player 2 Wins!!")
                play2Counter+=1
            elif(p2== "Paper"):
                print("Player 1 Wins!!")
                play1Counter+=1
print("\n")
print("=============================RESULT==============================")
if(play1Counter>play2Counter):
    print("Player 1 wins '{}' games out of '{}' games!!!".format(play1Counter,num))
elif(play1Counter<play2Counter):
    print("Player 2 wins '{}' games out of '{}' games!!!".format(play2Counter,num))
else:
    print("It's a tie !! Play Again ....")
print("=================================================================")

