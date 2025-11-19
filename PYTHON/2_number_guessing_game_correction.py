# Number Guessing Game

import random

def play():
    game_number = random.randint(1,10)
    attempts = 3
     
    while attempts > 0:
        try:
            player_number = int(input("Guess a number between 1 to 10 : "))
        except ValueError:
            print("Enter a valid number")
            continue 
            
        if game_number == player_number:
            print("You guessed correctly")
            break
        
        elif player_number < game_number:
            print("Too Low")
            
        elif player_number > game_number:
            print("Too high")
        
        attempts -= 1    
        print(f"Attempts left : {attempts}")   
        
        if attempts == 0:
            print("Game over", f"\nThe number was {game_number}")
      
play()

    
