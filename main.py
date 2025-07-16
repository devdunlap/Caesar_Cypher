import art

print(art.logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(original_text, shift_amount, direction):
    result_text = ""
    for char in original_text:
        if char in alphabet:
            original_index = alphabet.index(char)
            if direction == "encode":
                new_index = (original_index + shift_amount) % 26
            elif direction == "decode":
                new_index = (original_index - shift_amount) % 26
            else:
                new_index = original_index
            result_text += alphabet[new_index]
        else:
            result_text += char
    if direction == "encode":
        print(f"Here is the encoded result: {result_text}")
    elif direction == "decode":
        print(f"Here is the decoded result: {result_text}")
    else:
        print(result_text)

should_continue = True
while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    if direction not in ["encode", "decode"]:
        print("Error: Please enter 'encode' or 'decode' for the direction.")
    else:
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))
        caesar(text, shift, direction)
    restart = input("Type 'yes' if you want to go again. Otherwise type 'no':\n").lower()
    if restart != "yes":
        should_continue = False
        print("Goodbye!")