import random

word_list = ['Apple','Melon','Grapes','Banana','Cherry']

print(word_list)

def random_choice(word_list):
    '''
    Method takes a list of word and print random choise of the word
    :param word_list: List, words of list
    '''

    word = random.choice(word_list)

    print(word)





guess = input('Enter a single letter = ')

if len(guess) == 1 and guess.isalpha():

    print('Good guess!')

else:

    print('Oops! That is not a valid input')


   
    
    
