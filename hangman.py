import random

words = ["fire", "tiger", "house", "water", "plant"]
word = random.choice(words)

guessed = []
wrong_guesses = 0
max_wrong = 6

while wrong_guesses < max_wrong:
    display = ""

    for letter in word:
        if letter in guessed:
            display += letter + " "
        else:
            display += "_ "

    print("\nWord:", display)

    if "_" not in display:
        print(" Congratulations! You guessed the word:", word)
        break

    guess = input("Enter a letter: ").lower()

    if guess in guessed:
        print("You already guessed that letter.")
    elif guess in word:
        guessed.append(guess)
        print(" Correct!")
    else:
        guessed.append(guess)
        wrong_guesses += 1
        print("Wrong!")
        print("Remaining chances:", max_wrong - wrong_guesses)

if wrong_guesses == max_wrong:
    print("\n Game Over!")
    print("The word was:", word)
