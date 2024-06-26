import random


class Hangman():
    '''
    Hangman class which runs the game 
    '''
    def __init__(self, word_list, num_lives=5):
        '''
        Class constructor which initialize the hangman game
        '''
        self.word_list = word_list
        self.word = random.choice(word_list)
        self.word_guessed = ['_'] * len(self.word)
        self.num_letters = len(set(self.word))
        self.num_lives = num_lives
        self.list_of_guesses = []
        
    def check_guess(self, guess):
        '''
        Method checks the guess if is in the random word
        If the guess is in the word replace '_' in the word_guessed and reduce num_letter by 1
        If not in the word reduce the number of lives by 1
        :param guess:String
    
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
        '''
        method asks an input and iteratively checks if it is valid input
        if it is a single alphanumeric character checks the guess and append it to list of guesses
        '''
       
        while True:
            
            guess = input('Guess a letter: ')
            if len(guess) != 1  or not guess.isalpha():
                print('Invalid letter. Please, enter a single alphabetical character.')
            elif guess in self.list_of_guesses:
                print('You already tried that letter!')
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)
                print(self.word_guessed)
                break
                
def play_game(word_list):
    '''
    Creates and instance of a class Hangman
    Iteratively checks if number of lives equal 0.If so prints 'you lost!'
    :param word_list:List , list of words'''
    num_lives = 5
    game = Hangman(word_list, num_lives)

    while True:
        if game.num_lives == 0:
            print('You lost!')
            break
        elif game.num_letters > 0:
            game.ask_for_input()
            
        else:
            print('Congratulations!')
            break


if __name__=='__main__':
    word_list = ['apple','melon','grapes','banana','cherry']
    play_game(word_list)
    
    
   

