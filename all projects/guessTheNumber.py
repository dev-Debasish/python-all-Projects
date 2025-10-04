# this is the guess the number game 
# first import random to generate the random number between any range of numbers.
import random

#! generate the random number between 1 to 20
# secretNumber = random.randrange(1,20)
secretNumber = random.randint(1,20)

print("I am thinking of the number between 1 and 20")
# you have to guess the number within 6 guesses
for guessesTaken in range(1,7):
    print("Take a guess.")
    guess = int(input())

    if guess >  secretNumber:
        print("Your guess is too high")
    elif guess < secretNumber:
        print("Your guess is to low")
    else:
        break

if guess == secretNumber:
    print("good job! you guessed my number in",guessesTaken,"guesses")
else:
    print("nope! the number I was thinking of was",secretNumber)
