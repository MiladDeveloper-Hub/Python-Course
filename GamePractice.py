import random

print("Rock...")
print("Paper...")
print("Scissors\n")

player_2 = random.randint(0,2)
comMove = "rock"

if player_2 == 0:
    compMove = "rock"
elif player_2 == 1:
    compMove = "paper"
elif player_2 == 2:
    compMove = "scissors"

player_1_Wins = 0
player_2_Wins = 0
winScore = 3

while player_1_Wins < winScore and player_2_Wins < winScore :
    player_1 = input("Make Your move : ").lower()

    if player_1 == "q" or player_1 == "quit":
        break

    print(f"comp move is {comMove}")

    if comMove == player_1 :
        print("Tie")

    if player_1 == "rock":
        if comMove == "paper":
            print("Comp Win")
            player_2_Wins += 1
            player_2_Wins += 1
        elif comMove == "scissors":
            print("You win")
            player_1_Wins += 1
    elif player_1 == "paper":
        if comMove == "rock":
            print("You win")
            player_1_Wins += 1
        elif comMove == "scissors":
            print("Comp Win")
            player_2_Wins += 1
    elif player_1 == "scissors":
        if comMove == "rock":
            print("Comp win")
            player_2_Wins += 1
        elif comMove == "paper":
            print("You win")
            player_1_Wins += 1
    else:
        print("your enter a wrong word")

print(f"your score is {player_1_Wins} | copmuter score is {player_2_Wins}")