# STEP 1:  Welcome message

print("-----------------------------------\nThe Number Guessing Game\n-----------------------------------")
# Don't allow a blank name
name = input("Please tell us your coolest nickname: ")
while name == "":
    name = input("That was blank --- please tell us your coolest nickname: ")
print(f"Cool {name}!  Welcome to the gaunlet.")




# STEP 2:  Create randrange or randint 1-10

import random

number = random.randint(1,10)
# print(number)

# num = random.randrange(1,11)
# print(num)


# STEP 3:  While loop for guess till correct
# This step includes multiple parts:
# You need to prompt the player for a guess.
while True:
    try:
        guess = int(input("Please pick a number between 1 and 10: "))
#        print(guess)
    except ValueError:
        print(f"Are you learning impaired?  {name}, THROUGH 1 and 10!: ")
#        guess = int(input("Please pick a number between 1 and 10: "))
        continue
    break
# print(guess)

# You need to check their guess to see if it matches the random number.
# If the player is not correct, you need to ask them for a guess again.
# This continues until their guess matches the random number.

# STEP 4:  Tell user how many tries it took to guess the number correctly
# use guesses = guesses + 1 outside the while loop and += in if/else statement
guesses = 0
guesses = guesses +1

# STEP 5:  Account for potential errors.  < 1, > 10, 1,0, 1.0, one...
  # A vid on tube said to use isdigit, but I don't recall being taught that
  # I used another while loop above

while guess != number:
    if guess < 1 or guess > 10:
        print(f"{guess} is outside the scope.")
        guess = int(input("Please pick a number between 1 and 10:  "))
    elif guess < number:
#       print("Higher")
        guess = int(input("Higher:  "))
        guesses += 1
    elif guess > number:
#       print("Lower")
        guess = int(input("Lower:  "))
        guesses += 1
# I want exceptions for , (like 1,000), . (like 1.0), and one (string input by user) except:
#    except ValueError:
#        guess = int(print("You must type an integer 1 through 10, no decimals, commas, or strings:  "))

else:
    print("Nailed it!")
    if guesses == 1:
        print("It took you",guesses,"try","\nGame Over.")
    else:
        print("It took you",guesses,"tries","\nGame Over.")

"""
Was going to go for exceed expectations, but I found the highscore too hard to figure out.  
I was spinning my wheels and didn't want to cheat.  My plan is to edit the file on github 
when I learn it, then I'll have a more robust version of the code in my portfolio.  
For now, I've checked all the boxes to meet expectations, so 
it's time to move onto Unit 2. 
"""











"""
This function may work for play again, but the try block doesn't belong here (as was figured out in the most current attempt)
Play with this some more after I get more familiar with all this


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