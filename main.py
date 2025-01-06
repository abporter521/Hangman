from DictionaryUtils import Dictionary

STARTGAME = "    ___\n   /   \\\n   |\n   |\n __|___\n/      \\ "
HEAD = "    ___\n   /   \\\n   |   O\n   |\n __|___\n/      \\ "
BODY = "    ___\n   /   \\\n   |   O\n   |   |\n __|___\n/      \\ "
ARML = "    ___\n   /   \\\n   |   O\n   |  /|\n __|___\n/      \\ "
ARMR = "    ___\n   /   \\\n   |   O\n   |  /|\\ \n __|___\n/      \\ "
LEGL = "    ___\n   /   \\\n   |   O\n   |  /|\\ \n __|__/\n/      \\ "
FINISHGAME = "    ___\n   /   \\\n   |   O\n   |  /|\\ \n __|__/ \\\n/      \\ "

GAME=[STARTGAME, HEAD, BODY, ARML, ARMR, LEGL, FINISHGAME]

def play_game(secretword:str):
    hidden_word = list('_' * len(secretword))
    indexed_letters = list(secretword.lower())
    wrong_guesses = 0

    while wrong_guesses < len(GAME):
        print(GAME[wrong_guesses])
        print(' '.join(hidden_word))
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1:
            print("Guess a single letter only")
            continue
        
        if guess not in indexed_letters:
            print(f"The letter {guess} is not in the secret word")
            wrong_guesses += 1
            if wrong_guesses == len(GAME):
                print("You Lose")
            
        else:
            indices = [i for i, x in enumerate(indexed_letters) if x == guess]
            for i in indices:
                hidden_word[i] = guess
            
            if '_' not in hidden_word:
                print("YOU WIN")
                break
    
    while(True):
        new_game = input("Play again? (y/n): ").lower()
        if new_game == "y" or new_game == "n" or new_game == "yes" or new_game == "no":
            return new_game
            
            


if __name__ == "__main__":
    dictionary_loc = input("Please specify dictionary filepath: ")
    My_Dictionary = Dictionary(dictionary_loc)

    if not My_Dictionary.created:
        ValueError("Dictionary Not created")
        print("YIKES")
        exit(1)
    
    while(True):
        secretword = My_Dictionary.choose_word()

        if secretword.endswith('\n'):
            secretword=secretword.strip('\n')

        print(f'The secret word is {secretword}')

        again = play_game(secretword)
        if again == "n" or again =="no":
            break
        


