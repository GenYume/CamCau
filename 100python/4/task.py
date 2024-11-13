import random

choice = int(input("What do you choose ? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
comp = random.randint(0,2)

if choice == 0 :
    print("""
    _______
---'   ____)
        (_____)
        (_____)
        (____)
---.__(___)""")
elif choice == 1 :
    print("""
    _______
---'   ____)____
            ______)
            _______)
            _______)
---.__________)""")
elif choice == 2 :
    print("""
    _______
---'   ____)____
            ______)
        __________)
        (____)
---.__(___))""")
else :
    print("You didn't make a legal choice")


if comp == 0 :
    print("""
    _______
---'   ____)
        (_____)
        (_____)
        (____)
---.__(___)""")
elif comp == 1 :
    print("""
    _______
---'   ____)____
            ______)
            _______)
            _______)
---.__________)""")
elif comp == 2 :
    print("""
        _______
---'   ____)____
            ______)
        __________)
        (____)
---.__(___))""")

if choice == comp :
    print("It's a draw !")
elif choice == 0 :
    if comp == 1 :
        print("You lose !")
    else :
        print("You win !")
elif choice == 1 :
    if comp == 2 :
        print("You lose !")
    else :
        print("You win !")
elif choice == 2 :
    if comp == 0 :
        print("You lose !")
    else :
        print("You win !")
else :
    print("Play again ?")