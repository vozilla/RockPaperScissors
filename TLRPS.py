# Tuan Le
# Assignment 3: Final Project -- RPS Python Version
# Purpose: Creates an instance of a Rock, Paper, Scissors program
# Extra Credit: Python

import random

RPS = ['Rock', 'Paper', 'Scissors']
playerScore = 0
CPUScore = 0
menuLoop = True
gameCheck = False

# intro
print("Welcome to my program of Rock, Paper, Scissors!")

# menu loop
while menuLoop is True:
    playerYN = input("Would you like to play a game with me? (Y)es or (N)o? ")

    if playerYN is 'Y':
        menuLoop = False
        gameCheck = True
        playerInput = input("(r)ock, (p)aper, or (s)cissors, or (q)uit? ")

    elif playerYN is 'y':
        menuLoop = False
        gameCheck = True
        playerInput = input("(r)ock, (p)aper, or (s)cissors, or (q)uit? ")

    elif playerYN is 'N':
        menuLoop = False

    elif playerYN is 'n':
        menuLoop = False

    else:
        print("Invalid Input.")

# game loop
while gameCheck is True:
    CPU = random.RPS(RPS)
    if playerInput == CPU:
        print("\It's a draw!")
        print("We both picked " + str(CPU))

    elif(playerInput == 'r' and CPU == 's'):
        print("\nPlayer Wins")
        print("You Picked: Rock, CPU Picked: Scissors")
        playerScore += 1

    elif(playerInput == 'p' and CPU == 'r'):
        print("\nPlayer Wins")
        print("You Picked: Paper, CPU Picked: Rock")
        playerScore += 1

    elif(playerInput == 's' and CPU == 'p'):
        print("\nPlayer Wins")
        print("You Picked: Scissors, CPU Picked: Paper")
        playerScore+=1

    elif(CPU == 'r' and playerInput == 's'):
        print("\nCPU Wins")
        print("You Picked: Rock, CPU Picked: Scissors")
        CPUScore += 1

    elif(CPU == 'p' and playerInput == 'r'):
        print("\nCPU Wins")
        print("You Picked: Paper, CPU Picked: Rock")
        CPUScore += 1

    elif(CPU == 's' and playerInput == 'p'):
        print("\nCPU Wins")
        print("You Picked: Scissors, CPU Picked: Paper")
        CPUScore += 1

    elif(playerInput == 'Q'):
        gameCheck = False

    elif(playerInput == 'q'):
        gameCheck = False

    print("Player " + str(playerScore) + " || " + str(CPUScore) + " CPU")

# scores

print("Final Score:")
print("Player " + str(playerScore) + " || " + str(CPUScore) + " CPU")

print("Thanks for Playing!")
