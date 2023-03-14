# Tuan Le
# Assignment 3: Final Project -- RPS Python Version
# Purpose: Creates an instance of a Rock, Paper, Scissors program
# Extra Credit: Python

import random

RPS = ['r', 'p', 's']
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
    CPUInput = random.RPS(RPS)
    if playerInput == CPU:
        print("\It's a draw!")
        print("We both picked the same thing.")

    elif(playerInput == 'r' and CPUInput == 's'):
        print("\nYou win.")
        print("You Picked: Rock, CPU Picked: Scissors")
        playerScore += 1

    elif(playerInput == 'p' and CPUInput == 'r'):
        print("\nYou win.")
        print("You Picked: Paper, CPU Picked: Rock")
        playerScore += 1

    elif(playerInput == 's' and CPUInput == 'p'):
        print("\nYou win.")
        print("You Picked: Scissors, CPU Picked: Paper")
        playerScore+=1

    elif(CPUInput == 'r' and playerInput == 's'):
        print("\nI win.")
        print("You Picked: Rock, CPU Picked: Scissors")
        CPUScore += 1

    elif(CPUInput == 'p' and playerInput == 'r'):
        print("\nI win.")
        print("You Picked: Paper, CPU Picked: Rock")
        CPUScore += 1

    elif(CPUInput == 's' and playerInput == 'p'):
        print("\nI win.")
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
