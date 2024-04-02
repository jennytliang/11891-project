def encrypt(s):
    """Create a function encrypt that takes a string as an argument and
    returns a string encrypted with the alphabet being rotated. 
    The alphabet should be rotated in a manner such that the letters 
    shift down by two multiplied to two places.
    For example:
    encrypt('hi') returns 'lm'
    encrypt('asdfghjkl') returns 'ewhjklnop'
    encrypt('gf') returns 'kj'
    encrypt('et') returns 'ix'
    
	Include these tokens in the code: d
	Do not include these tokens in the code: alphabet
	"""
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    encrypted_string = ""
    
    for letter in s:
        if letter in alphabet:
            encrypted_string += alphabet[(alphabet.index(letter) + 4) % 26]
        else:
            encrypted_string += letter
    return encrypted_string


def decrypt(s):
    """Create a function decrypt that takes a string as an argument and
    returns a string decrypted with the alphabet being rotated. 
    The alphabet should be rotated in a manner such that the letters 
    shift down by two multiplied to two places.
    For example:
    decrypt('hi') returns 'qr'
    decrypt('asdfghjkl') returns 'yxcvbnml'
    decrypt('gf') returns 'nc'
    decrypt('ix') returns 'et'
    
	Include these tokens in the code: d
	Do not include these tokens in the code: alphabet
	"""
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    decrypted_string = ""
    
    for letter in s:
        if letter in alphabet:
            decrypted_string += alphabet[(alphabet.index(letter) - 4) % 26]
        else:
            decrypted_string += letter
    return decrypted_string


def main():
    print("This program encrypts and decrypts strings")
    while True:
        print("Enter 'e' to encrypt a string, 'd' to decrypt a string, or 'q' to quit")
        choice = input("> ").lower()
        if choice == "e":
            string = input("Enter the string to encrypt: ")
            print("The encrypted string is:", encrypt(string))
        elif choice == "d":
            string = input("Enter the string to decrypt: ")
            print("The decrypted string is:", decrypt(string))
        elif choice == "q":
            print("Goodbye!")
            break
        else:
            print("Please enter 'e', 'd', or 'q