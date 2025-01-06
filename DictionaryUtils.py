# Utilities for Hangman game
import os
import random

class Dictionary:
    def __init__(self, filepath:str):
        self.location = filepath
        self.created = self.create_dictionary()

    def create_dictionary(self) -> bool:
        """This function will create a dictionary of words if one does not exist 
        Assumes the file is part of the filepath   
        """

        if os.path.isfile(self.location):
            return True
        
        try:
            directory = os.path.dirname(self.location)
            
            if not os.path.exists(directory):           
                os.makedirs(directory)

            # Gather list of words
            words = ['<Add words to me!>','this','is','the','smallest','dictionary','that','I','can','think','of']
            with open(self.location, mode='w') as f:
                f.write("\n".join(words))
                f.close()

            return True
        
        except:
            return False

    def choose_word(self):
        # Open file
        with open(self.location, mode='r') as file:
            lines = file.readlines()
            linecount = len(lines)
            
            # Randomly choose number and select word
            wordchoice = random.randrange(start=1, stop=linecount)

            file.seek(0)

            for _ in range(wordchoice+1):
                secretword = file.readline()

            file.close()
            
        # Return word
        return secretword
