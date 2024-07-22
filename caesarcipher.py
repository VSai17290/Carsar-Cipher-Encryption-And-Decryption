



def encrypt(text, shift):
    result = ""
    # Iterate over each character in the input text

    for i in range(len(text)):
        char = text[i]
        # Check if the character is uppercase

        if char.isupper():
            # Shift the character and wrap around within the uppercase letters

            result += chr((ord(char) + shift - 65) % 26 + 65)
        # Check if the character is lowercase
        elif char.islower():
            # Shift the character and wrap around within the lowercase letters
            result += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            # If the character is not a letter, add it unchanged
            result += char
    return result

def decrypt(text, shift):
    
    # Decrypt by calling the encrypt function with a negative shift
    return encrypt(text, -shift)

def main():
    # Ask the user if they want to encrypt or decrypt
    choice = input("Do you want to (E)ncrypt or (D)ecrypt? ").upper()

    # Get the text to be processed from the user
    text = input("Enter the text: ")

    # Get the shift value from the user
    shift = int(input("Enter the shift value: "))

    # Check the user's choice
    if choice == 'E':
        # If the choice is to encrypt, call the encrypt function
        encrypted_text = encrypt(text, shift)
        print(f"Encrypted Text: {encrypted_text}")
    elif choice == 'D':
        # If the choice is to decrypt, call the decrypt function
        decrypted_text = decrypt(text, shift)
        print(f"Decrypted Text: {decrypted_text}")
    else:
        # If the choice is invalid, print an error message
        print("Invalid choice!")

# Ensure the main function is called when the script is run directly
if __name__ == "__main__":
    main()

