import art

print(art.logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

game_over = False

def caesar(direction, original_text, shift_amount):
    if direction == "decode":
        shift_amount = -shift_amount

    result = ""
    for letter in original_text:
        if letter in alphabet:
            shifted_letter = alphabet[(alphabet.index(letter)+shift_amount)%26]
            result += shifted_letter
        else:
            result += letter

    print(f"Here is the {direction}d result: {result}")
    

while not game_over:

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(direction, text, shift)

    play_again = input("Type 'yes' if you want to go again. Otherwise type 'no'\n").lower()
    if play_again == "no":
        print("Goodbye")
        game_over = True