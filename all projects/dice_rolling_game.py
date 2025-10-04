# dice_rolling _game 
#  adding some extra difficulty...

import random

count = 0
while(True):
    roll_dice = input("Roll the Dice? (y/n): ").lower()
    if (roll_dice == "y"):
        dice_no = int(input("How many dice you want to roll? "))
        for i in range(dice_no):
            dice1 = random.randint(1, 6)
            dice2 = random.randint(1, 6)
            print(f"Dice{i+1} = ({dice1}, {dice2})")
        count += 1
    elif(roll_dice == "n"):
        print("Thanks for playing!")
        break
    else:
        print("Invalid choice!")

print(f'You roll the dice {count} times.')  

