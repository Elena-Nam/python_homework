def make_hangman(secret_word):
    guesses = []
    def hangman_closure(letter):
        guesses.append(letter)

        # Build and print the current state of the guessed word
        display = ''
        for char in secret_word:
            if char in guesses:
                display += char
            else:
                display += '_'
        print(display)
         # Return True if all unique letters in the secret word have been guessed
        return all(char in guesses for char in set(secret_word))
    
    return hangman_closure


def main():
    secret_word = input("Enter the secret word: ").lower()

    game = make_hangman(secret_word)
    while True:
        guess = input("Guess a letter: ").lower()
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a letter.")
            continue

        done = game(guess)
        if done:
            print("Congratulations! You've guessed the word!")
            break

if __name__ == "__main__":
    main()