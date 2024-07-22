Caesar Cipher Encryption and Decryption Task
This repository contains an intern task assigned by Prodigy Infotech. The task involves implementing a Caesar cipher for the encryption and decryption of text. A Caesar cipher is a simple substitution cipher where each letter in the plaintext is shifted a certain number of places down or up the alphabet.
Table of Contents:
1) Introduction
2) Features
3) Prerequisites
4) Installation
5) Usage
6) Examples
7) Contributing
6) License
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

1) Introduction:
The Caesar cipher is a basic encryption technique used by Julius Caesar to securely communicate with his officials. In this task, you'll implement functions to both encrypt and decrypt messages using the Caesar cipher.

2) Features:
Encryption: Converts plaintext into ciphertext by shifting each letter by a specified number of positions.
Decryption: Converts ciphertext back into plaintext using the same shift value.

3) Prerequisites:
Python 3.x

4) Installation:
Clone the repository:

bash
Copy code
git clone <repository_url>
cd caesar-cipher-task
Ensure you have Python 3 installed. You can download it from python.org.

5) Usage
The repository includes two scripts: encrypt.py and decrypt.py.

Encryption
To encrypt a message, run the encrypt.py script with the plaintext and the shift value as arguments:

bash
Copy code
python encrypt.py "Your message here" <shift_value>
Decryption
To decrypt a message, run the decrypt.py script with the ciphertext and the shift value as arguments:

bash
Copy code
python decrypt.py "Encrypted message here" <shift_value>

6) Examples
Encrypting a Message
python
Copy code
# Running the encryption script
python encrypt.py "HELLO WORLD" 3

# Expected output: KHOOR ZRUOG
Decrypting a Message
python
Copy code
# Running the decryption script
python decrypt.py "KHOOR ZRUOG" 3

# Expected output: HELLO WORLD
Sample Code
You can also use the provided functions directly in your Python code:

python
Copy code
# encrypt.py
def encrypt(plaintext, shift):
    ciphertext = ""
    for char in plaintext:
        if char.isalpha():
            shift_base = 65 if char.isupper() else 97
            ciphertext += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            ciphertext += char
    return ciphertext

# decrypt.py
def decrypt(ciphertext, shift):
    return encrypt(ciphertext, -shift)

# Usage
plaintext = "HELLO WORLD"
shift = 3
ciphertext = encrypt(plaintext, shift)
print(f"Encrypted: {ciphertext}")  # Outputs: KHOOR ZRUOG

decrypted_message = decrypt(ciphertext, shift)
print(f"Decrypted: {decrypted_message}")  # Outputs: HELLO WORLD
7) Contributing
Contributions are welcome! Please fork this repository and submit pull requests. For major changes, please open an issue first to discuss what you would like to change.

8) License
This project is licensed under the MIT License. See the LICENSE file for details.
