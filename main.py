import random

def playGame(yourChoice, computer):
    if yourChoice not in ChoiceDict:
        while yourChoice not in ChoiceDict:
            print("Enter a valid choice!!")
            yourChoice = input("Enter Your choice(Snake S, Gun G, Water W): ").lower()
    
    print(f"Computer chose: {ChoiceDict[computer]}")
    print(f"You chose : {ChoiceDict[yourChoice]}")
    if computer == "s" and yourChoice == "g":
        return 1
    elif computer == "g" and yourChoice == "w":
        return 1
    elif computer == "w" and yourChoice == "s":
        return 1
    elif computer == "s" and yourChoice == "w":
        return 0
    elif computer == "g" and yourChoice == "s":
        return 0
    elif computer == "w" and yourChoice == "g":
        return 0
    else:
        return -1


def getWinner(userScore, computerScore):
    print(f"Your total score is {userScore} out of 5.")
    if userScore > computerScore:
        print("Hurrah!! You won the series!")
    elif userScore < computerScore:
        print("The Computer won the series,\nTry again! Better luck next time.")
    else:
        print(
            "It's a draw! Some rounds ended in a draw, resulting in an overall tie.\nWell played!"
        )


print("""You are playing Snake Water Gun game.
Rules are simple:
Snake wins over Water, Water wins over Gun and Gun wins over Snake
Same choices result in a draw.
There will be total 5 rounds in 1 match.
Good Luck! Score more and have fun!""")

ChoiceDict = {"s": "Snake", "w": "Water", "g": "Gun"}

userMood = "y"
while userMood.lower() == "y":
    userScore = 0
    computerScore = 0
    matchNo = 0
    while matchNo != 5:
        # Computer's Choice
        computer = random.choice(["s", "w", "g"])
        # Your Choice
        yourChoice = input(
                    "Enter your choice(Snake as S, Gun as G, Water as W): "
                ).lower()
        # Round result
        winner: int = playGame(yourChoice, computer)
        if winner == 1:
            print("You won!")
            userScore += 1
        elif winner == 0:
            print("Computer won!")
            computerScore += 1
        else:
            print("Draw!")
        matchNo += 1
    print("The 5-round match is over.")
    # Match result
    getWinner(userScore, computerScore)

    # Reinitialize
    userMood = input("If you want to play again, press 'Y'; otherwise, press any key.")

print("Thank You!!\nHope You enjoyed the Game.")
