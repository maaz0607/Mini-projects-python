# NUMBER GUESSING GAME 

import random
import sys

def game():
    print("Game has started")
    while True:
        difficulty=input("\nChoose a difficulty [1.EASY / 2.MEDIUM / 3.HARD]\nPress 1 for Easy\nPress 2 for Medium\nPress 3 for Hard.\nDifficulty: ")  
        max_guesses=0
        if difficulty.isdigit():
            difficulty=int(difficulty)
            if difficulty<=0:
                print("Enter valid difficulty.")

            elif difficulty==1:
                difficulty=2
                max_guesses=3
                break
            elif difficulty==2:
                difficulty=5
                max_guesses=6
                break
            elif difficulty==3:
                difficulty=10
                max_guesses=11
                break

            else:
                print("Enter valid difficulty level.")
        else:
            print("Enter valid integer.")
    target=random.randint(0,difficulty)
    guess_count=0
    while True:
        guess=input("\nEnter a guess: ")     
        if guess.isdigit():
            guess=int(guess) 
            guess_count+=1

            if guess==target:

                print("Your guess is correct")
                print("It took you",guess_count,"/",max_guesses,"tries to guess the number")
                break
            elif guess_count==max_guesses:
                print("Total number of guesses",max_guesses,"reached. You Lose.")
                sys.exit()
            elif guess>target:

                print("Your guess was higher than the target")
                print("Number of guesses",guess_count,"/",max_guesses)
            elif guess<target:

                print("Your guess was lower than the target")
                print("Number of guesses",guess_count,"/",max_guesses)
            
        else:
            print("Enter valid integer.")
        
            
            
print("--Number Guessing Game--")
while True:
    choice=input("\nDo you want to play (Y/N)\nEnter Y for yes and N for no\nInput= ")
    if choice.lower()=="y":
        
        print("Game Start")
        game()
        while True:
            
            choice2=input("\nDo you want to play again (Y/N)\nEnter Y for yes and N for no\nInput= ")
            if choice2.lower()=="y":
                game()
            
            elif choice2.lower()=="n":
                print("--Game exit--")
                sys.exit()
            else:#error? invalid response like 'maybe'
                print("\nInvalid input, please enter 'Y' or 'N' to start the game again \n Input: ")
        
    elif choice.lower()=="n":
        print("--Game exit--")
        break
    else:#error? invalid response like 'maybe'
        print("\nInvalid input, please enter 'Y' or 'N' to start the game.\n Input: ")
