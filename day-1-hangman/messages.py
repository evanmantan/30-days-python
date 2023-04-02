start_message = '''
Hello! Welcome to the Hangman game
==================================
In this game, you are going to be 
given a word. The catch is that
most of its letters are going to
be concealed.
You're going to be given 5 chances
to guess the letters. Good luck!'''

end_message = '''
===================
THANKS FOR PLAYING!
===================
'''

# hangmanpics source https://gist.github.com/chrishorton/8510732aa9a80a03c829b09f12e20d9c
hangmanpics = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']
