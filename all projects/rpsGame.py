# ROCK, PAPER, SCISSOR GAME
import random, sys
print("ROCK, PAPER, SCISSORS")
# variable to keep track of the no. of wins, losses and ties
wins = 0
losses = 0
ties = 0
# the main game loop
while True:
    # print("%s wins, %s losses, %s ties" %(wins, losses, ties))
    #! F-strings are generally faster than % formatting or .format().
    print(f"{wins} wins, {losses} losses, {ties} ties")

    # player input loop
    while True:
        print("Enter your move: (r)ock, (p)aper, (s)cissors or (q)uit")
        playerMove = input()
        if playerMove == 'q':
            sys.exit()    # quit the program 
        elif playerMove == 'r' or playerMove == 'p' or playerMove == 's':
            break    # break out of the player input loop   
        print("Type one of r, p, s or q")
    
    # display what the player choose
    if playerMove == 'r':
        print("ROCK versus")
    elif playerMove == 'p':
        print("PAPER versus")
    elif playerMove == 's':
        print("SCISSORS versus")

    # display what the computer choose
    randomNumber = random.randint(1,3)
    if randomNumber == 1:
        computerMove = 'r'
        print("ROCK")
    elif randomNumber == 2:
        computerMove = 'p'
        print("PAPER")
    elif randomNumber == 3:
        computerMove = 's'
        print("SCISSORS")
    
    # display the record the win/loss/tie:
    if playerMove == computerMove:
        print("It is a tie!")
        ties = ties + 1
    elif playerMove == 'r' and computerMove == 's':
        print("you Win!")
        wins  = wins + 1
    elif playerMove == 'p' and computerMove == 'r':
        print("you Win!")
        wins  = wins + 1
    elif playerMove == 's' and computerMove == 'p':
        print("you Win!")
        wins  = wins + 1
    elif playerMove == 's' and computerMove == 'r':
        print("you loss!")
        losses  = losses + 1
    elif playerMove == 'r' and computerMove == 'p':
        print("you loss!")
        losses  = losses + 1
    elif playerMove == 'p' and computerMove == 's':
        print("you loss!")
        losses  = losses + 1

