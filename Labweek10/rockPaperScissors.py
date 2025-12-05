# Name Lyle Osburne 11/10/2025
# Lab week 10
# Rock Paper Scissors game

import random

def generateComputerMove():
    return random.choice(["Rock", "Paper", "Scissors"])

def determineWinner(move1, move2):
    if move1 == move2:
        return "Draw"
    if move1 == "Rock" and move2 == "Scissors":
        return "Rock"
    if move1 == "Scissors" and move2 == "Rock":
        return "Rock"
    if move1 == "Paper" and move2 == "Rock":
        return "Paper"
    if move1 == "Rock" and move2 == "Paper":
        return "Paper"
    if move1 == "Scissors" and move2 == "Paper":
        return "Scissors"
    if move1 == "Paper" and move2 == "Scissors":
        return "Scissors"

def playRound(humanMove):
    computerMove = generateComputerMove()
    winner = determineWinner(humanMove, computerMove)
    if winner == "Draw":
        return "Draw!"
    if winner == humanMove:
        return "Human Wins!"
    else:
        return "Computer Wins!"

def main():
    rounds = int(input("How many rounds? (must be odd): "))
    while rounds % 2 == 0:
        rounds = int(input("Invalid. Enter an odd number: "))

    humanWins = 0
    computerWins = 0
    needed = (rounds // 2) + 1

    while humanWins < needed and computerWins < needed:
        move = input("Choose Rock, Paper, or Scissors: ")
        result = playRound(move)
        print(result)

        if result == "Human Wins!":
            humanWins += 1
        elif result == "Computer Wins!":
            computerWins += 1

    if humanWins > computerWins:
        print("You WIN the game!")
    else:
        print("The computer wins the game!")

if __name__ == "__main__":
    main()
