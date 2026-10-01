# main.py

from hangman import Hangman


def main():

    print("=" * 45)
    print("       🤖 HANGMAN CHATBOT GAME")
    print("=" * 45)

    game = Hangman()

    print("\n🤖 Bot: Welcome to Hangman!")
    print("🤖 Bot: Guess the hidden word one letter at a time.")

    while not game.is_won() and not game.is_lost():

        print("\n" + "-" * 45)

        print("🤖 Bot: Word:", game.display_word())
        print("🤖 Bot: Remaining attempts:", game.attempts)

        guess = input("👤 You: Enter a letter: ")

        message = game.guess_letter(guess)

        print("🤖 Bot:", message)

    print("\n" + "=" * 45)

    if game.is_won():
        print("🤖 Bot: 🎉 Congratulations! You won!")
        print("🤖 Bot: The word was:", game.get_word())
    else:
        print("🤖 Bot: 😢 Game Over!")
        print("🤖 Bot: The correct word was:", game.get_word())

    print("=" * 45)


if __name__ == "__main__":
    main()