"""
wordle.py
By: Adam, Ruben, Alex, BobTheBuilder
Citations: 
    https://gist.github.com/minism/1590432  - This was used for COLORS 
    https://github.com/Kinkelin/WordleCompetition/blob/main/data/official/shuffled_real_wordles.txt -  This was used for the imported TXT file
"""

import random

#DISCLAIMER BY YOURS TRULY: If the file and txt file are within a folder, ensure that you take it outside the folder and into the Explorer by dragging it down into where Python is actually running if your using VsCode.
    # TLDR: Drag it outside the folder!
"""

# C-Level Work:
# Letter  →  feeds into  →  color_guess()  →  feeds into  →  play_game()

# Class called (Letter):
    # Properties: (char), The single letter of the word, e.g. "a"
    # Properties: (color), The assigned color (GREEN, YELLOW, or GRAY)
    # Methods: (render()), This returns the color-coded string for this single letter
    # Objects: This is created inside color_guess(), one per character position in the guess
    
# B-Level Work:
# LOOK into PyGame and doing the Wordle on PyGame (similar to the turtle drawing lines activity earlier in the semester using Turtle).
    # The words on the screen shouldn't be clickable via the mouse (as shown in the NYTimes Wordle) as people rarely use them, and instead use the letter bank as a letter tracker. 

# A-Level Work:
# Using this Repo and FlowChart

"""
# COLORS
GREEN = "\033[42m" # The letter's in the right placement
YELLOW = "\033[43m" # The letter's in the word, not the right placement
GRAY = "\033[47m" # The letter is not in the word
RESET = "\033[0m" # This reset's the termianal background & text color back to colorless/default


class Letter:
    def __init__(self, char: str, color: str):
        """
        Represents a single letter in a guess.

        Properties:
            char  (str): The single character, e.g. "a"
            color (str): The assigned color (GREEN, YELLOW, or GRAY)
        """
        self.char = char
        self.color = color

    def render(self) -> str:
        """
        Returns the color-coded string for this letter.
        """
        return self.color + self.char + RESET
        
def load_wordlist(filepath: str = "real_wordles.txt") -> list[str]: 
    """
    Loads words from a text file.

    Parameters:
        filepath (str): A path is created to the wordlist found in the text file

    Returns:
        list[str]:  A list of stripped/lowercased words found in the wordlist 
    """
  
    with open(filepath, "r") as f: # This opens the file in read mode.

        return [line.strip().lower() for line in f if line.strip()] # This returns each line/word  within the txt file as a lowercase string


def validate_guess(guess: str, word_length: int = 5) -> bool: 
    """
    This function validates wheter the guess is wrong or right

    Parameters:
        guess (str):       The word entered by the player
        word_length (int): The length of a word and or guess, default is 5

    Returns:
        bool: True if the guess length matches word_length, prints an error messages if the guess is invalid 
    """
    if len(guess) != word_length: #Checks if the guess is not the required length. 
        print(f"Incorrect length, it must be {word_length} letters") #Prints an error message telling the player the required length of the word. 
        return False # Returns False since it was invalid 
    return True #Returns True if the length of the guess was correct. 


def color_guess(guess: str, secert: str) -> str: 
    """
    Builds a color-coded string by comparing each letter of the guess to the secret.
    Green  = correct letter, correct position.
    Yellow = correct letter, wrong position.
    Gray   = letter not in the word.

    This function dictates wheter a letter is correct or not, using color coded strings

    Green  = The correct place and letter
    Grey   = A letter that's not in the word 
    Yellow = The correct letter, however it's in the wrong position

    Parameters:
        guess (str): The word guessed by the player
        secret   (str): The secret target word aka the correct word needed

    Returns:
        str: A string with  color codes applied to each letter of the guess validating whether it's wrong, 
        right or in the wrong place
    """
    output = ""
    for i in range(len(guess)):  #This loops through each of the 5 letter positions
        if guess[i] == secert[i]:  #Checks if the guessed letter matches the secrets letter
            letter = Letter(guess[i], GREEN) # This creates a Letter object with GREEN
        elif guess[i] in secert: #Checks if the guessed letter exists in the secret word
            letter = Letter(guess[i], YELLOW) # This creates a Letter object with YELLOW
        else: 
            letter = Letter(guess[i], GRAY)    # If the letter is not within the word, it'll creat a Letter object with GRAY
        output += letter.render() # Calls Letter's method, render() 
    return output #Returns the colored response


def get_guess(word_length: int = 5) -> str: #STANDALONE
    """
    Repeatedly prompts the player for input until a valid guess is entered.

    Parameters:
        word_length (int):  The length of a word and or guess, default is 5

    Returns:
        str: A lowercased guess string of the exact length of characters
    """
    while True: # Keeps looping until a valid guess is entered
        try:
            guess = input("Enter current guess: ").lower() # Tells the player to input a guess and converts input to lowercase
        except KeyboardInterrupt:  # Catches Ctrl+C so the game doesn't crash
            print("\nQuitting...")
            exit(0)
        if validate_guess(guess, word_length):
            return guess


def play_game(wordlist: list[str], max_attempts: int = 5, word_length: int = 5) -> None: #STANDALONE
    """
    This function runs the game from start to finish

    Parameters:
        wordlist     (list[str]):  The list that contains the words you pick
        max_attempts (int):       The amount of guesses you are allowed, default is 5 but can be changed
        word_length  (int):       The length of a word and or guess, default is 5

    Returns:
        None: The game is printed to the terminal and ends when you guess right or run out of guesses.
    """

    secret:str = random.choice(wordlist)
    attempts:str = max_attempts

    print("LET'S PLAY WORDLE!")
    print(f"Your purpose is to guess {word_length}-letter word. You have up to 5 tries before you lose. \n")

    try:
        while attempts > 0:
            guess = get_guess(word_length)
            print(color_guess(guess, secret))

            if guess == secret:
                print("You guessed correctly, you win!")
                return

            attempts -= 1
            print("Tries left:", attempts)

    except KeyboardInterrupt:
        print(f"\nGame quit early. The word was: {secret}")
        exit(0)

    print("Game over! Your word was:", secret)


if __name__ == "__main__":
    wordlist = load_wordlist("real_wordles.txt")
    play_game(wordlist)

