# This is a deductive logic game where we guess a number based on clues
# We are given 10 tries to get the guess correct

import random

NUM_DIGITS = 3
MAX_GUESSES = 10

def main():
    print(''' Bagels is a deductive logic game.
          
          I am thinking of a {} -digit number with no repeated digits.
          Try to guess what it is. Here are some clues:
          
          When I say:       That means:
          Pico              One digit is correct but in the wrong position
          Fermi             One digit is correct and in the right position
          Bagels            No digit is correct

          For example, if the secret number was 248 and your guess was 843, the clues 
          would be Fermi Pico.'''.format(NUM_DIGITS))
    
    # Creating the main game loop
    while True:
        # Storing the secret number the player needs to guess
        secretNum = getSecretNum()
        print('I have thought up a secret number')
        print('You have {} guesses to get it .'.format(MAX_GUESSES))

        num_guesses = 1
        while num_guesses <= MAX_GUESSES:
            guess = ''
            # We keep looping until the user gets the correct guess
            while len(guess) != NUM_DIGITS or not guess.isdecimal():
                print('Guess #{}: '.format(num_guesses))
                guess = input('> ')
            
            # Setting up the loop for the clues
            clues = getClues(guess, secretNum)
            print(clues)

            if guess == secretNum:
                break # Break out of this loop since the number is correct
            if num_guesses == MAX_GUESSES:
                print('You ran out of guesses')
                print('The answer was {}.'.format(secretNum))
            num_guesses += 1
            
        # Ask the player if they want to play again
        print('Do you want to play again? (yes or no)')
        if not input('> ').lower().startswith('y'):
            break
    print('Thanks for playing!')

def getSecretNum():
    # Creating the random number generator
    NUMBERS = list('1234567890')
    random.shuffle(NUMBERS)

    # Get the first num_digits in the list for the secret number
    secretNum = ''

    for i in range(NUM_DIGITS):
        secretNum += str(NUMBERS[i])
    return secretNum

def getClues(guess, secretNum):
    # returns the string with the different clues
    if guess == secretNum:
        return 'You got it right!'

    clues = []

    for i in range(len(guess)):
        if guess[i] == secretNum [i]:
            # A correct digit is in the correct spot
            clues.append('Fermi')
        elif guess[i] in secretNum:
            # A correct digit is in the wrong spot
            clues.append('Pico')
    
    if len(clues) == 0:
        # There are no correct digits at all
        return 'Bagels'
    else:
        # Sort the clues in alphabetical order 
        # So the original order does not give information away
        clues.sort()
        # Make a single string from the list of string clues
        return ' '.join(clues)
    
# How to run the game
if __name__ == '__main__':
    main()