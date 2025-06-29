import random

def get_random_word():
    words = ['python', 'hangman', 'challenge', 'programming', 'openai', 'developer', 'computer', 'science']
    return random.choice(words)

def display_game_state(word, guesses, tries_left):
    display_word = ' '.join([letter if letter in guesses else '_' for letter in word])
    print(f"Word: {display_word}")
    print(f"Tries Left: {tries_left}")
    print(f"Guessed letters: {' '.join(sorted(guesses))}")

def hangman():
    word = get_random_word()
    guesses = set()
    tries_left = 6

    print("Welcome to Hangman!")
    print("Guess the word one letter at a time.")
    
    while tries_left > 0:
        display_game_state(word, guesses, tries_left)
        guess = input("Enter your guess (single letter): ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single alphabetic letter.\n")
            continue

        if guess in guesses:
            print(f"You already guessed '{guess}'. Try a different letter.\n")
            continue

        guesses.add(guess)

        if guess in word:
            print(f"Good guess! '{guess}' is in the word.\n")
        else:
            tries_left -= 1
            print(f"Sorry, '{guess}' is not in the word.\n")

        # Check if all letters are guessed
        if all(letter in guesses for letter in word):
            print(f"Congratulations! You correctly guessed the word: {word}")
            break
    else:
        print(f"Game over! You've run out of tries. The word was: {word}")

if _name_ == "_main_":
    hangman()