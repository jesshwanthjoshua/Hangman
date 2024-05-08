import random
from hangman_art import logo
import hangman_words
import hangman_art

print(logo)
print("Welcome to Hangman Game.")
chosen_word = random.choice(hangman_words.word_list)
display = []
lives = 6

for x in chosen_word:
    display.append("_")
print(display)
print(hangman_art.stages[lives])

while lives > 0:
    print(f"Chosen word is {chosen_word}")
    print(f"pending lives: {lives}\n")
    guess = input("guess the letter: ").lower()
    temp_count = 0

    for position in range(len(chosen_word)):
        if guess == chosen_word[position]:
            temp_count += 1
            display[position] = guess

    print(display)
    if temp_count >= 1:
        print(f"\nCorrect Guess. Proceed to guess the rest.\n\n")

    else:
        lives -= 1
        print(f"\nWrong Guess. Chance lost, You lose a life.\n\n")
        print(hangman_art.stages[lives])

    exist_count = display.count("_")
    if exist_count == 0 and lives > 0:
        lives = 0
        word = ""
        for letters in display:
          word += letters
        print("You've Won.")
        print(f"The word is {word}.")  

    elif lives == 0:
        print("You've lost all lives. Game Over.")
