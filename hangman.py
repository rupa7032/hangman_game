# hangman.py
from words import get_random_word
class Hangman:
    def __init__(self):
        self.word = get_random_word()
        self.guessed_letters = set()
        self.attempts = 6
    def display_word(self):
        result = ""
        for letter in self.word:
            if letter in self.guessed_letters:
                result += letter + " "
            else:
                result += "_ "
        return result.strip()
    def guess_letter(self, letter):
        letter = letter.lower()
        if len(letter) != 1 or not letter.isalpha():
            return "Please enter only one letter."

        if letter in self.guessed_letters:
            return "You already guessed this letter."

        self.guessed_letters.add(letter)

        if letter in self.word:
            return f"Correct! '{letter}' is in the word."
        else:
            self.attempts -= 1
            return f"Wrong! '{letter}' is not in the word."

    def is_won(self):
        return all(
            letter in self.guessed_letters
            for letter in self.word
        )
    def is_lost(self):
        return self.attempts <= 0
    def get_word(self):
        return self.word