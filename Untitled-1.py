
import random
print("number guessing Game")
number = random.randint(1, 9)
chances = 0
print("Think of a number between 1-9, and type it into the system")
while chances < 5:
    guess = int(input("Input your number here:  "))
    if guess == number:
        print("You guessed the correct number!")
        break
        print("The number you gave was too low. Guess a number higher than", guess)
        print("The number you gave was too high. Try thinking of a number lower than", guess)
    chances += 1
if not chances < 5:
    print("You lost. To try again, reload the program.", number)