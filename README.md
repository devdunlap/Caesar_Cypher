
# Caesar Cipher

A simple interactive Python program to encrypt and decrypt messages using the classic Caesar cipher technique.

## Features
- Encode (encrypt) and decode (decrypt) messages with a shift value
- Handles both uppercase and lowercase letters
- Leaves numbers, spaces, and punctuation unchanged
- Robust input validation and error handling
- ASCII art banner for a fun user experience
- Option to repeat the process as many times as you like

## How It Works
The Caesar cipher shifts each letter in your message by a specified number of positions in the alphabet. For example, with a shift of 3, 'A' becomes 'D', 'B' becomes 'E', etc. Decoding reverses the process.

## Usage
1. Run `main.py` in your terminal:
	```bash
	python main.py
	```
2. Follow the prompts:
	- Choose to encode or decode
	- Enter your message
	- Enter a shift number (1-25 recommended)
	- View the result
	- Choose to go again or exit

## Example
```
Type 'encode' to encrypt, type 'decode' to decrypt:
encode
Type your message:
Hello, World!
Type the shift number (1-25 recommended):
3

📝 Original text: Hello, World!
🔒 Encoded result: Khoor, Zruog!
🔄 Shift amount: 3
```

## Files
- `main.py` — Main program logic and user interface
- `art.py` — Contains the ASCII art logo

## Requirements
- Python 3.x

No external dependencies required.

---

Enjoy encrypting and decrypting your secret messages!
