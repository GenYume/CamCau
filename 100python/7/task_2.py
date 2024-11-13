import random

word_list = ["learn", "clean", "plan"]

chosen_word = random.choice(word_list)
# print(chosen_word)

placeholder = ""
for l in chosen_word:
    placeholder += "_"

print(placeholder)


# TODO-1 - Use a while loop to let the user guess again
# TODO-2 - Change the for loop so that you keep the previous correct guesses

display = ""

while display != chosen_word:
    guess = input("Guess a letter : ").lower()
    display = ""
    for i in range(0, len(chosen_word)):
        if guess == chosen_word[i]:
            display += guess
        elif placeholder[i] != "_":
            display += placeholder[i]
        else:
            display += "_"
    placeholder = display

    print(display)