import random
import nltk
nltk.download('words')
from nltk.corpus import words
words.
i = random.choice(words.words())

# prints 236736
print(len(word_list))




word_list = ['python', 'java', 'kotlin', 'javascript']

# Defining class

class Hangman:

    def __init__(self, word_list, tries):
        self.word = random.choice(word_list)
        self.list = list(self.word)
        self.hidden = "-" * len(self.word)
        self.letters = set(self.word)
        self.already_guessed = []
        self.tries = tries

    def guess(self, letter):
        if len(letter) != 1:
            print("You should input a single letter")
        elif letter != letter.lower() or not letter.isalpha():
            print("It is not an ASCII lowercase letter")
        elif letter in self.already_guessed:
            print("You already typed this letter")
        elif letter in self.letters:
            for i in range(len(self.word)):
                if self.word[i] == letter:
                    list_hidden = list(self.hidden)
                    list_hidden[i] = letter
                    self.hidden = "".join(list_hidden)
            self.already_guessed.append(letter)
        else:
            self.tries -= 1
            print("No such letter in the word")
            self.already_guessed.append(letter)

    def play(self):
        while True:
            if self.tries == 0:
                print("You lost!")
                break
            elif self.word == self.hidden:
                print("You survived!")
                break
            else:
                print("\n" + self.hidden)
                letter = input("Input a letter: ")
                self.guess(letter)

# Deploying the game:

print('H A N G M A N')

while True:
    choice = input('Type "play" to play the game, "exit" to quit: ')
    if choice == 'play':
        hangman = Hangman(word_list, 8)
        hangman.play()
    elif choice == 'exit':
        break
    else:
        print("Error")