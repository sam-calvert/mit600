# 6.00 Problem Set 3
# 
# Hangman
#


# -----------------------------------
# Helper code
# (you don't need to understand this helper code)
import random
import string

WORDLIST_FILENAME = "words.txt"

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print(("  ", len(wordlist), "words loaded."))
    return wordlist

def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# actually load the dictionary of words and point to it with 
# the wordlist variable so that it can be accessed from anywhere
# in the program


wordlist = load_words()

# your code begins here!

def list_to_string(lst):
    string = ""
    for i in lst:
        string += i
    return(string)

def hangman():
    word = choose_word(wordlist)
    ans = []
    guessed_letters = []
    for letter in word: 
        ans.append(letter)
        guessed_letters.append("_")
    avail_letters = string.ascii_lowercase
    guesses_remaining = 8
    
    print("Welcome to the game, Hangman! \n\
    I am thinking of a word that is %d letters long" % len(ans))
    while True:
        print("--------------------")
        print("You have %d guesses left" % guesses_remaining)
        print("Available letters: %s" % avail_letters)
        new_guess = input("Please guess a letter: ")
        if new_guess not in ans:
            guesses_remaining -= 1
            if guesses_remaining < 1:
                print("sorry, you lose.")
                print("the answer was %s" % word)
                return()
            print(("Oops! That letter is not in my word: %s" % list_to_string(guessed_letters)))
        elif new_guess in guessed_letters:
            print("You already guessed that!")
        else:
            for i in range(len(ans)):
                if ans[i] == new_guess:
                    guessed_letters[i] = new_guess
            print("Good guess: %s" % list_to_string(guessed_letters))
            if "_" not in guessed_letters:
                print("Congratulations, you won!")
                return()
        avail_letters = avail_letters.replace(new_guess,"")
hangman()
