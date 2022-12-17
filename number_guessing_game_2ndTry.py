# STEP 1:  Welcome message

print("-----------------------------------\nThe Number Guessing Game\n-----------------------------------")
name = input("Please tell us your coolest nickname: ")
print(f"Cool {name}!  Welcome to the gaunlet.")


# STEP 2:  Create randrange or randint 1-10

import random

number = random.randint(1,10)
print(number)

# num = random.randrange(1,11)
# print(num)


# STEP 3:  While loop for guess till correct
# This step includes multiple parts:
# You need to prompt the player for a guess.

guess = int(input("Please pick a number between 1 and 10:  "))

# You need to check their guess to see if it matches the random number.
# If the player is not correct, you need to ask them for a guess again.
# This continues until their guess matches the random number.

# STEP 4:  Tell user how many tries it took to guess the number correctly
# use guesses = guesses + 1 outside the while loop and += in if/else statement
guesses = 0
guesses = guesses +1

# STEP 5:  Account for potential errors.  < 1, > 10, 1,0, 1.0, one...
while guess != number:
    if guess < 1 or guess > 10:
        print("That number is outside the scope.")
        guess = int(input("Please pick a number between 1 and 10:  "))
    elif guess < number:
 #       print("Higher")
        guess = int(input("Higher:  "))
        guesses += 1
    elif guess > number:
#        print("Lower")
        guess = int(input("Lower:  "))
        guesses += 1
else:
    print("Nailed it!")
    if guesses == 1:
        print("It took you",guesses,"try","\nGame Over.")
    else:
        print("It took you",guesses,"tries","\nGame Over.")

















"""
# def play_game():
guesses = 0
guesses = guesses +1
while guess != number:
    try:
        if guess < 1 or guess > 10:
            print("That number is outside the scope.")
            guess = int(input("Please pick a number between 1 and 10:  "))
        elif guess < number:
            print("Higher")
            guess = int(input(f"{name}, please pick a number between 1 and 10:  "))
            guesses += 1
        elif guess > number:
            print("Lower")
            guess = int(input(f"{name}, please pick a number between 1 and 10:  "))
            guesses += 1
    except ValueError:
        print("\nCome on Dude, no commas, no garbage, just a whole number from 1 to 10")
    except NameError:
        print("\nCome on Dude, integers/numbers not strings/words")
else:
    print("Nailed it!")
    if guesses == 1:
        print("It took you",guesses,"try")
    else:
        print("It took you",guesses,"tries")
#play_game()
"""





"""
highscore = guesses
while 
"""




"""
# prior attempt 

import random 

number = random.randint(1,10)
guess = int(input("guess a #: "))

# I think that's right

while guess != number:
    if guess > 10:
        raise ValueError("That number is out of scope.  Please choose a number from 1 to 10: ")
    if guess < 1:
        raise ValueError("That number is out of scope.  Please choose a number from 1 to 10: ")
    if guess == float(""):
        raise ValueError("Invalid literal; must be a whole number")
    if guess > number:
        print("lower:  ")
    else:
        print("higher:  ")
        guess = int(input("guess again????????????????  "))
print("nailed it, the number is",number)

# I think that's about what I did before
"""