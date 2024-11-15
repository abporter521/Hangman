# Utilities for Hangman game
import os
import random

def create_dictionary(filepath:str) -> bool:
    """This function will create a dictionary of words if one does not exist 
       Assumes the file is part of the filepath   
    """

    if os.path.exists(filepath):
        return True
    
    if not os.path.exists(filepath):
        #TODO: MAKE FILEPATH
        os.makedirs(filepath)

        # Gather list of words
        f = open(filepath, mode="w")
        f.write("<Add words to me!>\nthis\nis\nthe\nsmallest\ndictionary\nthat\nI\ncan\nthink\nof")
        f.close()
        return True

    return False

def choose_word(filepath:str):

    # Open file
    with open({filepath}, mode='r') as file:
        lines = file.readlines()
        linecount = len(lines)
        
        # Randomly choose number and select word
        wordchoice = random.randrange(start=1, stop=linecount)

        for _ in range(wordchoice):
            secretword = file.readline()

        file.close()
        
    # Return word
    return secretword
