import random
import time
from messages import start_message, end_message, hangmanpics

filepath = 'words.txt'
words = []

def read_txt(filepath):
    """Read file then return list of words"""
    with open(filepath) as f:
        text = f.read()
    words = text.split('\n')
    words = [w for w in words if len(w) > 1] # make sure that there's no blank entry
    return words

def wipe():
    """Function to clear screen"""
    print("\033[H\033[J", end="")
    
def pick_word(words):
    """Pick a word randomly then remove it from the list"""
    word = random.choice(words)
    words.remove(word)
    return word.upper()

def conceal(word):
    """Make a concealed copy of the word"""
    concealed_word = ['_' if i.isalpha() else ' ' for i in word]
    return concealed_word

def ask_player(word, concealed_word):
    """Query player for answer"""
    answer = str(input('Guess a lettter: ')).upper()
    if answer in word:
        for i in range(len(word)):
            if word[i] == answer:
                concealed_word[i] = answer
        return True, concealed_word
    else:
        return False, concealed_word
    
def game_running():
    """Function that stores the logic while game is running"""
    playing = True
    points = 0
    words = read_txt(filepath)
    while playing == True:
        tries = 0 # Reset number of tries every new game
        word = pick_word(words)
        concealed_word = conceal(word)
        while True:
            wipe()
            print('Points =', points)
            print(hangmanpics[tries], '\n', flush=True)
            if (tries == 6) : # User loses the game
                time.sleep(2)
                return
            for i in concealed_word:
                print(i, end='')
            print('\n')
            if ''.join(concealed_word) == word.upper(): # User guesses correctly
                points += 1
                while True:
                    play = str(input('Continue playing? (Y/N) '))
                    if play.upper() == 'Y':
                        break
                    elif play.upper() == 'N':
                        playing = False
                        break
                    else:
                        print('Only answer with Y or N please')
                        time.sleep(2)
                        wipe()
                break
            correct, concealed_word = ask_player(word, concealed_word)
            if not correct:
                tries += 1

def game_end():
    """Function that is called when the game ends"""
    wipe()
    print(end_message)
    
def start_game():
    """Main function to start the game"""
    print(start_message)
    game_running()
    game_end()

start_game()
