def check_guess(guess):
    
    if guess.lower() in word:
        print(f"Good guess!{guess} is in the word.")
    else:
        print(f"Sorry,{guess} is not in the word. Try again.")

def ask_for_input():
    
    while True:

       guess = input("Guess a letter:")
       if guess.isalpha():
           
           break
    print("Invalid letter. Please, enter a single alphabethical character.") 

    check_guess(guess)
    
ask_for_input()



            
