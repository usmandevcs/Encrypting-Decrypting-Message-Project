# Encrypting & Decrypting Messages project
'''
This project allows users to encrypt and decrypt messages using a 
simple substitution cipher (cipher means a method of encrypting messages). 
The user can choose to either encrypt a message by substituting each 
letter with another letter, or decrypt a message by reversing the substitution 
process. The program will prompt the user for the message and the key 
(the substitution alphabet) to perform the desired operation.
'''
import random
import string

chars = " " + string.punctuation + string.digits + string.ascii_letters
chars = list(chars)
key = chars.copy()
random.shuffle(key)

print(f"chars: {chars}")
print(f"key: {key}")

print("Welcome to the Encrypting & Decrypting Messages program!")

def encrypt(message, key):
    encrypted_message = ""
    for char in message:
        if char in chars:
            index = chars.index(char)
            encrypted_message += key[index]
        else:
            encrypted_message += char
    return encrypted_message
def decrypt(encrypted_message, key):
    decrypted_message = ""
    for char in encrypted_message:
        if char in key:
            index = key.index(char)
            decrypted_message += chars[index]
        else:
            decrypted_message += char
    return decrypted_message
def main():
    while True:
        choice = input("Do you want to (E)ncrypt or (D)ecrypt a message? (E/D): ").upper()
        if choice == 'E':
            message = input("Enter the message to encrypt: ")
            encrypted_message = encrypt(message, key)
            print(f"Encrypted message: {encrypted_message}")
        elif choice == 'D':
            encrypted_message = input("Enter the message to decrypt: ")
            decrypted_message = decrypt(encrypted_message, key)
            print(f"Decrypted message: {decrypted_message}")
        else:
            print("Invalid choice. Please enter 'E' for encrypt or 'D' for decrypt.")
        continue_choice = input("Do you want to continue? (Y/N): ").upper()
        if continue_choice != "Y":
            print("Thank you for using the Encrypting & Decrypting Messages program. Goodbye!")
            break

if __name__ == "__main__":
    main()
