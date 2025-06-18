import random

def hangman():
    words = ["apple", "pizza", "chair", "light", "movie"]
    word = random.choice(words)
    guessed_letters = []
    tries = 6
    display = ["_" for _ in word]

    print("Welcome to Hangman!")

    while tries > 0 and "_" in display:
        print("\nWord:", " ".join(display))
        guess = input("Guess a letter: ").lower()

        if guess in guessed_letters:
            print("You already guessed that letter.")
        elif guess in word:
            print("Correct!")
            for i in range(len(word)):
                if word[i] == guess:
                    display[i] = guess
            guessed_letters.append(guess)
        else:
            print("Incorrect!")
            tries -= 1
            guessed_letters.append(guess)
            print(f"Tries left: {tries}")

    if "_" not in display:
        print("\nYou won! The word was:", word)
    else:
        print("\nGame Over! The word was:", word)

hangman()