
"""
Main module for Caesar Cipher program.
Handles user interaction and cipher logic.
"""

import art

print(art.LOGO)
alphabet = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
    'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]


def caesar(original_text, shift_amount, direction):
    """
    Encrypts or decrypts a message using the Caesar cipher.
    Args:
        original_text (str): The message to encode or decode.
        shift_amount (int): The number of positions to shift.
        direction (str): 'encode' or 'decode'.
    """
    result_text = ""
    for char in original_text:
        # Handle lowercase letters
        if char.lower() in alphabet:
            original_index = alphabet.index(char.lower())
            if direction == "encode":
                new_index = (original_index + shift_amount) % 26
            elif direction == "decode":
                new_index = (original_index - shift_amount) % 26
            else:
                new_index = original_index
            # Preserve original case (uppercase/lowercase)
            new_char = alphabet[new_index]
            if char.isupper():
                new_char = new_char.upper()
            result_text += new_char
        else:
            # Keep spaces, numbers, punctuation unchanged
            result_text += char
    # Display results with better formatting
    print(f"\n📝 Original text: {original_text}")
    if direction == "encode":
        print(f"🔒 Encoded result: {result_text}")
    elif direction == "decode":
        print(f"🔓 Decoded result: {result_text}")
    else:
        print(f"Result: {result_text}")
    print(f"🔄 Shift amount: {shift_amount}")

SHOULD_CONTINUE = True
while SHOULD_CONTINUE:
    # Get valid direction with error recovery
    while True:
        user_direction = input(
            "Type 'encode' to encrypt, type 'decode' to decrypt:\n"
        ).lower().strip()
        if user_direction in ["encode", "decode"]:
            break
        print("❌ Error: Please enter exactly 'encode' or 'decode' for the direction.")
        print("Example: encode (to encrypt) or decode (to decrypt)\n")

    # Get message text
    text = input("Type your message:\n")

    # Get valid shift number with error recovery
    while True:
        shift_input = input("Type the shift number (1-25 recommended):\n").strip()
        try:
            shift = int(shift_input)
            if shift < 0:
                print("❌ Warning: Negative shift will work but consider using positive numbers.")
            break
        except ValueError:
            print(f"❌ Error: '{shift_input}' is not a valid number.")
            print("Please enter a whole number (e.g., 1, 5, 13, 25)\n")

    # Run the caesar cipher
    caesar(text, shift, user_direction)

    # Ask to restart with error recovery
    while True:
        restart = input(
            "\nType 'yes' if you want to go again. Otherwise type 'no':\n"
        ).lower().strip()
        if restart in ["yes", "y", "no", "n"]:
            break
        print("❌ Error: Please enter 'yes' or 'no' (or just 'y' or 'n')")

    if restart in ["no", "n"]:
        SHOULD_CONTINUE = False
        print("👋 Goodbye! Thanks for using the Caesar Cipher!")
    else:
        print("\n" + "=" * 50 + "\n")  # Visual separator for new session
