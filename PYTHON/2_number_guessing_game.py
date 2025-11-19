# Number Guessing Game

import random

def play():
     game_number = random.randint(1,10)
     player_number = int(input("Guess a number between 1 to 10 : "))

     if game_number == player_number:
         print("You guessed correctly")
         replay()
     else:
         while player_number != game_number:
             player_number = int(input("Guess again : "))
             if game_number == player_number:
                 print("You guessed correctly")
                 replay()
        
def replay():
    play_again = input("Play again ? (yes/no) :")
    if play_again == "yes":
        play()
    else:
        quit()
        
play()

'''        
while player not guessed correctly 
ask player guess
if player guess correctly 
out of loop 

play again option
Ask to play again
If player accept 
play


exit option
'''
    
