import milestone_2

word = milestone_2.random_choice(milestone_2.word_list)

def check_guess(guess):
    '''
    checks the guessed letter if in the word
    :param guess:String, a single guessed letter
    '''


    guess = guess.lower()
    


    if guess in word:


        print(f'Good guess!{guess} is in the word.')


    else:


        print(f'Sorry,{guess} is not in the word. Try again.')

def ask_for_input():
    '''
    Iteratively checks if the input is a valid guess
    '''
    
    while True:

       guess = input('Guess a letter:')

       if len(guess) == 1 and guess.isalpha():
           
           
           break
       
       else:
          
          print('Invalid letter. Please, enter a single alphabethical character.') 

    check_guess(guess)

ask_for_input()



            
