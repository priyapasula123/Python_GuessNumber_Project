import random

def play_number_guessing_game():
    print("\n===== NUMBER GUESSING GAME =====\n")
    print("I'm thinking of a number between 1 and 100.")
    print("Try to guess it in as few attempts as possible!")
    print("To exit the game at any time, type 'exit' or 'quit'.\n")
    
    number = random.randint(1, 100)
    attempt = 1
    
    try:
        guess_input = input("Guess the Number: ")
        
        # Check if user wants to exit
        if guess_input.lower() in ['exit', 'quit']:
            print("Thanks for playing! Goodbye!")
            return
            
        guess = int(guess_input)
        
        while True:
            if guess > number:
                guess_input = input("Guess another number. This one is too big: ")
                # Check if user wants to exit
                if guess_input.lower() in ['exit', 'quit']:
                    print("Thanks for playing! Goodbye!")
                    return
                guess = int(guess_input)
                attempt += 1
            elif guess < number:
                guess_input = input("Guess another number. This one is too small: ")
                # Check if user wants to exit
                if guess_input.lower() in ['exit', 'quit']:
                    print("Thanks for playing! Goodbye!")
                    return
                guess = int(guess_input)
                attempt += 1
            else:
                print(f"Yeah that's the number! You guessed it right in {attempt} attempts.")
                
                # Ask if the user wants to play again
                play_again = input("\nDo you want to play again? (yes/no): ")
                if play_again.lower() in ['yes', 'y']:
                    play_number_guessing_game()  # Recursively start a new game
                else:
                    print("Thanks for playing! Goodbye!")
                return
    
    except ValueError:
        print("Invalid input! Please enter a number between 1 and 100.")
        play_number_guessing_game()  # Restart the game on invalid input

if __name__ == "__main__":
    play_number_guessing_game()
