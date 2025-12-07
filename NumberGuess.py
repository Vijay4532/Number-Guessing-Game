import random
import os
def clear_screen():
    if os.name=="nt":
        os.system('cls')
    else:
        os.system('clear')

def show_welcomme_message():
    """Displays the game banner and instructions."""
    print("\n")
    print("="*50)
    print("NUMBER GUESSING GAME")
    print("="*50)
    print("I am thinking of a number between 1 and 100.")
    print("Can you guess What it is")
    print("="*50)
def set_difficulty():
    """Asks the user to select a difficulty level."""
    while True:
        level=input("\nChoose difficulty. Type 'easy' or 'medium' or 'hard': ").lower()
        if level=='easy':
            return 10
        elif level=='medium':
            return 7
        elif level=="hard":
            return 3
        else:
            print("Invalid choice! Please type 'easy' or 'medium' or 'hard'.")
def play_game():
    """Main logic of the game."""
    clear_screen()
    show_welcomme_message()
    secret_number=random.randint(1,100)
    total_attempts=set_difficulty()
    remaining_attempts=total_attempts
    print(f"\nYou have {remaining_attempts} attempts to guess the number.")

    guess=0
    while remaining_attempts>0:
        try:
            print(f"\nAttempts remaining: {remaining_attempts}")
            guess_input=input("Enter your guess: ")
            guess=int(guess_input)
            if guess<secret_number:
                print("Too Low! Try a higher number.")
            elif guess>secret_number:
                print("Too High! Try a lower number.")
            else:
                print("\n"+"*"*50)
                print(f"CONGRATULATIONS You Guessed {secret_number}!")
                print(f"You used {total_attempts-remaining_attempts+1} attempts.")
                print("*"*50+"\n")
                return
            
            remaining_attempts-=1
        except ValueError:
            print("Invalid input! Please enter a valid number.")
    print("\n"+"x"*50)
    print(f"GAME OVER! You ran out of attempts.")
    print(f"The secret number was: {secret_number}")
    print("x"*50+"\n")

while True:
    play_game()
    play_again=input("Do you want to play again? (yes/no): ").lower()
    if play_again!="yes":
        print("\nThanks for playing! Goodbye.\n")
        break

