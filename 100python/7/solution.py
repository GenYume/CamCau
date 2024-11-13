import random
import hangman_words
import hangman_art


word_list = hangman_words.word_list

chosen_word = random.choice(word_list)

placeholder = ""
for l in chosen_word:
    placeholder += "_"

stages = hangman_art.stages

print(hangman_art.logo)

lives = 6

game_over = False
correct_letters = []
guesses = []

while not game_over:
    print(f"You have {lives} lives left !")
    guess = input("Guess a letter : ").lower()

    if guess in guesses:
        print(f"You've already guessed {guess}")
    else:
        display = ""
        for letter in chosen_word:
            if guess == letter:
                display += letter
                correct_letters.append(guess)
            elif letter in correct_letters:
                display += letter
            else:
                display += "_"

    if guess not in chosen_word and guess not in guesses:
        print(f"You guessed {guess}, that's not in the word.\nYou lose a life")
        lives -= 1
    
    guesses.append(guess)

    if lives == 0:
        game_over = True
        print(f"You lose ! The word was '{chosen_word}'")
    
    
    print(display)    

    print(stages[lives])

    if "_" not in display:
        game_over = True
        print("You win !")
