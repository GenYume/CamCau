import random

word_list = ["learn", "clean", "plan"]

# TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word. Then print it.

chosen_word = random.choice(word_list)
print(chosen_word)

# TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

guess = input("Guess a letter : ").lower()
print(guess)

# TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word. Print "Right" if it is, "Wrong" if it's not.

for l in range(0, len(chosen_word)):
    if guess == chosen_word[l]:
        print("Right")
    else:
        print("Wrong")

# TODO-1 - Create a "placeholder" with the same number of blanks as in the chosen_word

placeholder = ""
for l in chosen_word:
    placeholder += "_"

print(placeholder)
# TODO-2 - Create a "display" with that puts the guess letter in the right positions and _ in the wrong one.

display = ""

for i in chosen_word:
    if guess == i:
        display += guess
    else:
        display += "_"

print(display)