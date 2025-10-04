#  import the required modules for the development of the game 
import sys, random
# print the introductory line for the game
print("ROCK, PAPER, SCISSOR")
# declear the required variables to keep track of the no. of wins, losses, ties..
wins = 0
losses = 0
ties = 0


#  main game loop
while True:
    print(f'{wins} WINS, {losses} LOSSES, {ties} TIES')
    # player input loop
    while True:
        print("Enter your move: (r)ock, (p)aper, (s)cissors or (q)uit")
        playerMove = input()
        if playerMove == 'q':
            sys.exit()   # quit the program
        elif (playerMove == 'r' or playerMove == 'p' or playerMove == 's'):
            break      # break out of the player Input loop
        print("Type one of r, p, s or q")
    
    #  display what the player choose
    if playerMove == 'r':
        print("ROCK VERSUS")
    elif playerMove == 'p':
        print("PAPER VERSUS")
    elif playerMove == 's':
        print("SCISSOR VERSUS")
        
    # DISPLAY THE COMPUTER MOVE
    randomNumber = random.randint(1, 3)
    if randomNumber == 1:
        computerMove = 'r'
        print("ROCK")
    elif randomNumber == 2:
        computerMove = 'p'
        print("PAPER")
    elif randomNumber == 3:
        computerMove == 's'
        print("SCISSOR")
        
    # display the records and the other staff that is essential for the program
    
    
        
    
    