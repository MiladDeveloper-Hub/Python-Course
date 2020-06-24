import random


def good():
    print("\n\nGood Bye Hero, Thanks To Play My Game ! :)\n")

def final():
    print(f"\nFinal Scores :\n\t\t\t  You : {youWins}\n\t\t\t  Computer : {computerWins}")

def Help():
    print("\nHelp : Enter ( Exit ) To Exit Game")

def Movemake():
    print("\nRock, Paper, Scissors\n\tWhich ?? ")

def startgame():
    print("\nHello User To My Game ! ... :)")
    print("\nRock...@\nPaper...[]\nScissors.../\\\n")


# Start Game

startgame()

randomNumber = random.randint(0, 2)
computerMove = "rock"

timeDast = int(input("How many to play game ?? "))
Help()
Movemake()

if randomNumber == 0:
    computerMove = "Rock"
elif randomNumber == 1:
    computerMove = "Paper"
elif randomNumber == 2:
    computerMove = "Scissors"



youWins = 0
computerWins = 0
winScore = 5
dast = 0

while dast < timeDast:
    User = input("\nPlease Make Your Move : ").lower()

    if User == "Exit".lower():
        print("\nYou Exit From Game !... :(")
        break

    print(f"Computer Move is : {computerMove}")
    Computer = computerMove

    if User.lower() == Computer.lower():
        print("\nResult : Tie :) ...")
        dast += 1

    if User == "rock":
        if Computer == "Paper":
            computerWins += 1
            print("\nResult : Computer Win ! ...")
            dast += 1
        elif Computer == "Scissors":
            youWins += 1
            print("\nResult : You Win ! ...")
            dast += 1
    elif User == "paper":
        if Computer == "Rock":
            youWins += 1
            print("\nResult : You Win ! ...")
            dast += 1
        elif Computer == "Scissors":
            computerWins += 1
            print("\nResult : Computer Win ! ...")
            dast += 1
    elif User == "scissors":
        if Computer == "Rock":
            computerWins += 1
            print("\nResult : Computer Win ! ...")
            dast += 1
        elif Computer == "Paper":
            youWins += 1
            print("\nResult : You Win ! ...")
            dast += 1
    else:
        print("\nResult : You Enter A Wrong Word :( ...\n")

final()
good()

# End Game
