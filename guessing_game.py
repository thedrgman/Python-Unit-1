"""
Python Web Development Techdegree
Project 1 - Number Guessing Game
--------------------------------

"""

import random
# Set minimum and maximum values that will be used for the range
MAX = 10
MIN = 1


def start_game():
    play = "y"
    highscore = 0
    while play != "n" or play != "no": # This helps keep the game going until the player inputs no or n, at the moment it is y because they want to play, why else would they be here.
        print("---------------------------------------------------------------")
        print("              Welcome to the Number Guessing Game")
        print("   Just follow the instructions and we'll have a lot of fun")      # Welcoming them to the game and letting them know we will have a lot of fun
        print("---------------------------------------------------------------")
        random_num = random.randrange(MIN,MAX) #Random number generated
        attempts = 1 # Counts of how many attempts it is for them guess correctly
        
        if highscore != 0:
            print("Highscore to beat is: {}".format(highscore)) # Used to display highscore after each completed round
            
        guess = num_guess(0) # Function used for picking the number and it catches any errors there may be
        
        while guess != random_num: # This goes on until the correct answer is picked
            if guess > MAX or guess < MIN: # If their guess is outside the range it catches it and has them try again.
                print("Sorry your guess was out of range. Please try again")
                guess = num_guess(guess)
            elif guess > random_num:
                print("It's Lower") # This lets them know that their guess was too low
                attempts += 1 # Everytime they miss the number of attempts go up
                guess = num_guess(guess)
            elif guess < random_num:
                print("It' Higher") # This lets them know that their guess was too high
                attempts += 1
                guess = num_guess(guess)
        print("Good Job and Game Over") # Game is finish and congradulates them
        print("It took you {} attempts!   ".format(attempts)) # Displays number of attempts is took them
        
        if attempts < highscore: #This checks to see if they beat their highscore and then displays the highscore.
            highscore = attempts
        elif highscore == 0:
            highscore = attempts
        print("Highscore is: ", highscore)
        play = input("Would you like to play again?   [Y]es or [N]o?  ").lower() # Checks with them if they would like to play again

        
def num_guess(num):
    while True: # This loops through until an input is given that is a number
        try:
            num = int(input("Pick a number between {} and {}!   ".format(MIN,MAX)))
            break
        except ValueError:
            print("Sorry that was not a number between {} and {}.   ".format(MIN,MAX))
            continue
    return num




start_game()
