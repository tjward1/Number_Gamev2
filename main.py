# Taylor Ward
# Purpose: Create a number guessing game
# update the number guessing game to include a list of top 5 players

from library import updateFile
# import random module to generate random number for game
from random import randint


# initialize variables
numGuess = 0
guess = ""
inGame = 0

print("\n======== NUMBER GAME ========")
# ask for user's name
myName = input("Please enter your name: ")

# iterate through the loop to let the user keep playing the game
while inGame == 0:
    # generate random integer between 1 & 100 inclusive
    myNumber = randint(1, 100)
    # debug - print random number chosen so I can accurately assess my code
    # print(f"{myNumber}")

    print(f"Hello {myName}, I'm thinking of a number between 1 and 100... Guess what it is!\n")

    # ask for another guess as long as the guess is not correct
    while True:
        try:
            # ask user to guess a number
            guess = input("Your guess: ")

            # allow the user to exit the game at any time by entering q
            if guess == 'q':
                print(f"\nSorry to see you go {myName}! My number was {myNumber}!")
                inGame = 1
                break
            # only guesses between 1 and 100 are valid
            elif 1 <= int(guess) <= 100:
                # count the number of guesses (only the valid ones)
                numGuess = int(numGuess) + 1
                if int(guess) > myNumber:
                    print("Too high! Try again or enter q to quit\n")
                elif int(guess) < myNumber:
                    print("Too low! Try again or enter q to quit\n")
                # when user answers correctly, give number of guesses and start new game
                else:
                    print(f"\nThat's correct! Yay! \nIt only took you {numGuess} guesses!")
                    # when user guesses correctly, call function that writes to the leaderboard file
                    updateFile(numGuess, myName)
                    print("\nGame starting over...")
                    # put at default value for number of guesses
                    numGuess = 0
                    break
            else:
                # guess was not between 1 and 100
                print("Reminder: Please choose an integer between 1 and 100\n")

        # catch exceptions so that the user can keep playing
        # for the EOFError, catch it but still let the user exit the game
        except EOFError as e:
            print(f"\nSorry to see you go {myName}! My number was {myNumber}!")
            inGame = 1
            break
        except ValueError as e:
            print(f"Invalid input. Please choose a number between 1 and 100!\n")
        except Exception as e:
            print(f"Error occurred: {e}")
            break

print("Game over!")
