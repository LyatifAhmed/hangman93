from milestone_4 import Hangman
from milestone_2 import word_list
def play_game(word_list):
    num_lives = 5
    game = Hangman(word_list,num_lives)
    while True:
        if num_lives == 0:
            print('You lost!')
        elif num_letters > 0:
            ask_for_input()
        elif num_lives != 0 and num_letters <= 0:    
            print('Congratulations. You won the game!')

play_game(word_list)            
