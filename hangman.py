import random
def play_hangman():
    # Setup hidden word and game variables
    words_pool = ["python", "developer", "program", "hangman", "coding"]
    word = random.choice(words_pool)
    guessed_letters = []
    incorrect_guesses = 0
    MAX_INCORRECT_GUESSES = 6
    # Game loop running while guesses remain
    while incorrect_guesses < MAX_INCORRECT_GUESSES:
        # Generate the hidden word display (e.g., p _ t h _ n)
        display_word = " ".join([letter if letter in guessed_letters else "_" for letter in word])
        
        print(f"\nWord: {display_word}")
        print(f"Incorrect guesses remaining: {MAX_INCORRECT_GUESSES - incorrect_guesses}")
        
        # Check for win condition
        if all(letter in guessed_letters for letter in word):
            print(f"\nYou win! The word was '{word}'.")
            return

        # Get player input
        guess = input("Guess a letter: ").strip().lower()

        # Validate input
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter one letter.")
        elif guess in guessed_letters:
            print("You already guessed that letter.")
        else:
            guessed_letters.append(guess)
            
            if guess in word:
                print("Good guess!")
            else:
                incorrect_guesses += 1
                print("That letter is not in the word.")

    # If the loop finishes without returning, the player loses
    print(f"\nGame over! The word was '{word}'.")

if __name__ == "__main__":
    play_hangman()