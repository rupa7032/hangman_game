# words.py
WORDS = [
    "python",
    "computer",
    "programming",
    "developer",
    "algorithm",
    "database",
    "software",
    "technology",
    "keyboard",
    "internet",
    "hangman",
    "machine",
    "network",
    "education",
    "student"
]
def get_random_word():
    import random
    return random.choice(WORDS)