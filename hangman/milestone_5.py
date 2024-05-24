import random
from milestone_2 import word_list
class Hangman():
    '''
    The hangman class and methods
    '''
    def __init__(self, word_list, num_lives=5):
        self.word_list = word_list
        self.word = random.choice(word_list)
        self.word_guessed = list('_' * len(self.word))
        self.num_letters = len(self.word)
        self.num_lives = num_lives
        
        self.list_of_guesses = list()
        
    def check_guess(self, guess):
        '''
        
        '''

        guess = guess.lower()
        
        
        if guess in self.word:
            print(f'Good guess! {guess} is in word.')
            for index, letter in enumerate(self.word):
                if letter == guess:
                    self.word_guessed[index] = letter
            self.num_letters -= 1   
        else:
            self.num_lives -= 1
            print(f'Sorry,{guess} is not in the word')   
            print(f'You have {self.num_lives} lives left')
                


            
            

    def ask_for_input(self):
       
        while True:
            print(self.word_guessed)
            guess = input('Guess a letter: ')
            if len(guess) != 1  or not guess.isalpha():
                print('Invalid letter. Please, enter a single alphabetical character.')
            elif guess in self.list_of_guesses:
                print('You already tried that letter!')
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)
        
def play_game(word_list):
    num_lives = 5
    game = Hangman(word_list, num_lives)

    while True:
        if num_lives == 0:
            print('You lost!')
        elif game.num_letters > 0:
            game.ask_for_input()
        else:
            print('Congratulations!')

play_game(word_list)
   

