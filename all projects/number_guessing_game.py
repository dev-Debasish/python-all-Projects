import random

computer_guess = random.randint(1, 100)
count = 0

while True:
    try:
        user_guess = int(input("Guess the number between 1 and 100: "))
        if (1 <= user_guess <= 100):
            if computer_guess > user_guess:
                print("Too High!")
            elif computer_guess < user_guess:
                print("Too Low!")
            else:
                print("Congratulation! You guessed the number.")
                break
        else:
            raise Exception("Number out of bound!")
    except ValueError:
        print("Please enter a valid number.")
    
    count += 1

print(f"you guessed the number in {count + 1} attempts!")
    
    