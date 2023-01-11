
"""
Python Web Development Techdegree
Project 1 - Number Guessing Game
---------------------------------

For this first project we will be using Workspaces.

NOTE:  If you strongly prefer to work locally on your own computer, you can totally do that by clicking: File -> Download Workspace in the file menu after you fork the snapshot of this workspace.

    Psuedo-code Hints
    
    When the program starts, we want to:
    ------------------------------------
    1. Display an intro/welcome message to the player.
    2. Store a random number as the answer/solution.
    3. Continuously prompt the player for a guess.
       a. If the guess greater than the solution, display to the player "It's lower".
       b. If the guess is less than the solution, display to the player "It's higher".  
    4. Once the guess is correct, stop looping, inform the user they "Got it"
         and show how many attempts it took them to get the correct number.
    5. Let the player know the game is ending, or something that indicates the game is over.
    
    ( You can add more features/enhancements if you'd like to. )
"""

import random
import time


def guessing_game():
    print("-----------------------------------\nThis is...\n\n")
    time.sleep(2)
    print("The Number Guessing Game")
    time.sleep(1)
    print("\n\n-----------------------------------")
    guesses = 0
    guesses += 1
    number = random.randint(1,10) # alt number = random.randrange(1,11)
#    print(number)
    guess = ""
    while guess != number:
        try:
            guess = int(input(f"{name}, please pick a number between 1 and 10:  "))
            if guess < 1 or guess > 10:
                print("freakin frack")
            elif guess < number:
                guesses += 1
                print("Higher")
            elif guess > number:
                guesses += 1
                print("Lower")
                continue
        except ValueError:
            print("Integers only.")
            continue
#    except ValueError as err:
#        print(err,"---> INTEGERS (1-10) ONLY!")
#        pass
        except NameError:
            print("Integers only.")
            continue
    else:
        print(f"Nailed it, {name}!")
        if guesses == 1:
            print("That took you",guesses, "legit guess and that concludes this game.")
        else:
            print("That took you",guesses, "legit guesses ad that concludes this game.")

"""
        answer = input("Would you like to play again? y/n ")
            if answer == "y":
                guessing_game()
            else:
                print("h.a.n.d.")
"""

name = input("Please tell us your coolest nickname: ")
while name == "":
    name = input("That was blank --- please tell us your coolest nickname: ")
time.sleep(1)
print(f"Cool {name}!")
time.sleep(1)
answer = input("Would you like to play a game? y/n ")
if answer.lower() == "y":
    print("Welcome to the gauntlet")
    guessing_game()
else:
    print("h.a.n.d.")











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