# import random 
# import sys

# user_score = 0
# computer_score = 0
# while True:
#     user_choice = input("Rock, Paper, Scissor? (r/p/s): ").lower()
#     if user_choice == 'r':
#         print("You choose 🪨")
#     elif user_choice == 'p':
#         print("You choose 📃")
#     elif user_choice == 's':
#         print("You choose ✂️")
#     else:
#         print("Invalid choice!")
#         sys.exit()


#     computer_choice = random.randint(1, 3)
#     if computer_choice == 1:
#         computer_choice = 'r'
#         print("Computer choose 🪨")
#     elif computer_choice == 2:
#         computer_choice = 'p'
#         print("Computer choose 📃")
#     elif computer_choice == 3:
#         computer_choice = 's'
#         print("Computer choose ✂️")
        

#     if(computer_choice == user_choice):
#         print("Its Draw")
#     elif (user_choice== 'r' and computer_choice == 'p'):
#         print("You Lose :<")
#         computer_score += 1
#     elif (user_choice== 'r' and computer_choice == 's'):
#         print("You Win :>")
#         user_score +=1
#     elif (user_choice== 'p' and computer_choice == 'r'):
#         print("You win :>")
#         user_score += 1
#     elif (user_choice== 'p' and computer_choice == 's'):
#         print("You Lose :<")
#         computer_score += 1
#     elif (user_choice== 's' and computer_choice == 'p'):
#         print("You Win :>")
#         user_score += 1
#     elif (user_choice== 's' and computer_choice == 'r'):
#         print("You lose :<")
#         computer_score += 1


#     further_game_on = input("Continue? (y/n): ").lower()
#     if (further_game_on == 'n'):
#         break
    

# print(f"Your score {user_score}")
# print(f"computer score {computer_score}")
# if(user_score > computer_score):
#     print("yeahh!! You Win, Computer loose,")
# elif(user_score < computer_score):
#     print("Opps!! Computer Win, You loose,")
# else:
#     print("At last, NoBody Win")
    
    
    
#!!!! another approach (Better)


import random

ROCK = 'r'
PAPER = 'p'
SCISSOR = 's'

#?  to map the value for each choice we use dictionary
emojis = {ROCK: '🪨', PAPER: '📃', SCISSOR: '✂️'}
#?  we store the value in tuple as tuple is immutable 
# choices = ('r', 'p', 's')
choices = tuple(emojis.keys())

while True:
    user_choice = input("Rock, Paper, Scissor? (r/p/s): ").lower()
    if user_choice not in choices:
        print("Invalid Choice!")
        continue  #! ****
    computer_choice = random.choice(choices)

#*  this next line throws error if we put any invalid value, because the dictionary emojis not have any key regarding the invalid input value ,,
#!  that why we use {continue} to skip the next iteration  after the invalid choice statement 
    print(f"Your Choice {emojis[user_choice]}")
    print(f"Computer Choice {emojis[computer_choice]}")
    
    if user_choice == computer_choice:
        print("Tie!")
    elif(
        (user_choice == ROCK and computer_choice == SCISSOR) or
        (user_choice == SCISSOR and computer_choice ==PAPER) or
        (user_choice == PAPER and computer_choice ==ROCK)):
        print("You win")
    else:
        print("You lose")
        
    should_continue = input("Continue? (y/n): ").lower()
    if (should_continue == 'n'):
        break
    


# put the related code into a function to make the program little more clear and handy
