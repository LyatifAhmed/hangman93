
import milestone_2
import milestone_3
import random
class Hangman():
    def __init__(self, word_list, num_lives=5):
        self.word = random.choice(word_list)
        self.word_guessed = ['_' * len(self.word)]
        self.num_letters = len(self.word)
        self.num_lives = num_lives
        self.word_list = word_list
        self.list_of_guesses = []
        
    def check_guess(self, guess):
        guess = guess.lower()
        if guess in self.word:
            print(f'Good guess! {guess} is in word.')
            for letter in self.word:
                if letter == guess:
                    self.word_guessed[letter] = letter
            self.num_letters -= 1   
        else:
            num_lives -= 1
            print('Sorry,{letter} is not in the word')   
            print('You hasve {num_lives} lives left')     


            
            

    def ask_for_input():
       
        while True:
            guess = input('Guess a letter: ')
            if len(guess) > 1  and  guess.isalpha():
                print('Invalid letter. Please, enter a single alphabetical character.')
            elif guess in self.list_of_guesses:
                print('You already tried that letter!')
            else:
                check_guess(guess)
                self.list_of_guesses.append(guess)
    ask_for_input()
                  












        
            
        