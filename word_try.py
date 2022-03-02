import random
computer = ("Rock", "Paper", "Scissors")
game = random.choice(computer)
while True:
    move = input("Make your choice! Rock, Paper or Scissors? ")
    if str(move) == game:
        print(f"{game}! It's a tie")
    elif str(move) == "Rock" and game == "Paper":
        print(f"{game}! You lose")
    elif str(move) == "Rock" and game == "Scissors":
        print(f"{game}! You win!")
        Again = input ("Want to play again? Y or N: ")
        if str(Again) == "Y":
            print("Let's do it!")
        else:
            break
    elif str(move) == "Paper" and game == "Scissors":
        print(f"{game}! You lose!")
    elif str(move) == "Paper" and game == "Rock":
        print(f"{game}! You win!")
        Again = input ("Want to play again? Y or N: ")
        if str(Again) == "Y":
            print("Let's do it!")
        else:
            break
    elif str(move) == "Scissors" and game == "Rock":
        print(f"{game}! You lose!")
    elif str(move) == "Scissors" and game == "Paper":
        print(f"{game}! You win!")
        Again = input ("Want to play again? Y or N: ")
        if str(Again) == "Y":
            print("Let's do it!")
        else:
            break