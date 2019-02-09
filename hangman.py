'''
OBJECTIVE: 
We want to create a game that will allow us to play hangman on our computer
ALGORRITHM:
First, randomly select a word from the created text dictionary
Second, use the input from the user to tell whether he/she guessed a letter correct
Third, turn what the user enters into a string 
Created on Nov 29, 2018

@author: ITAUser
'''

'''
This function brings in a text file and returns a random word from it
'''
def pick_random_word():
    f = open("words.txt", 'r')
    words = f.readlines()
    index = random.randint(0, len(words) - 1)
    word = words[index].strip()
    return word
'''
Function takes input from user for the next letter
'''
def ask_user_for_next_letter():
    letter = input("Guess your letter: ")
    return letter.strip().upper()
'''
function will create a string of letters guessed correctly and underscores for letters not yet guessed
'''
def generate_word_string(word, letters_guessed):
    output = []
    for letter in word:
        if letter in letters_guessed:
            output.append(letter.upper())
        else:
            output.append("_")
    return " ".join(output)
import random

'''
checks that the module we are using is currently the main module
'''
if __name__ == '__main__':
    WORD = pick_random_word()
    
    letters_to_guess = set(WORD)
    correct_letters_guessed = set()
    incorrect_letters_guessed = set()
    num_guesses = 0
    
    print("Welcome to Hangman!")
    
    '''
    calls the pick_random_word() function and assigns word to string variable WORD
    '''
    while (len(letters_to_guess) > 0) and num_guesses < 6:
    
        '''
        makes input from user equal to variable guess and set guess to lowercase version of self
        '''
        guess = ask_user_for_next_letter()
        guess = guess.lower()
        
        '''
        checks if user's guess was guessed already
        '''
        if guess in correct_letters_guessed or \
                guess in incorrect_letters_guessed:
            print("You already guessed that letter.")
            continue
        
        ''' checks if letter is in letters_to_guess'''
        if guess in letters_to_guess:
            letters_to_guess.remove(guess)
            correct_letters_guessed.add(guess)
        else:
            incorrect_letters_guessed.add(guess)
            num_guesses += 1
        
        word_string = generate_word_string (WORD, correct_letters_guessed)
        print(word_string)
        print("You have {} guesses left".format(6 - num_guesses))
        
        ''' Conditional that lets user know if they won or not and what the word is'''
        if num_guesses < 6:
            print ("Congratulations! You correctly guessed the word")
        else:
            print("Sorry, you lose! Your word was {}".format(WORD))

    
