def encode(message):
    """
    Write a function that takes a message, and encodes in such a 
    way that it swaps case of all letters, replaces all vowels in 
    the message with the letter that appears 2 places ahead of that 
    vowel in the english alphabet. 
    Assume only letters. 
    
    Examples:
    >>> encode('test')
    'TGST'
    >>> encode('This is a message')
    'tHKS KS C MGSSCGG'
    
	Include these tokens in the code: def switch _ case ( ch ): if
	"""
    vowels = ['a', 'e', 'i', 'o', 'u']
    encoded_message = ''
    for letter in message:
        if letter in vowels:
            index = vowels.index(letter)
            if index < len(vowels) - 2:
                encoded_message += vowels[index + 2]
            else:
                encoded_message += vowels[index - 2]
        else:
            if letter.isupper():
                encoded_message += letter.lower()
            else:
                encoded_message += letter.upper()
    return encoded_message


def decode(message):
    """
    Write a function that takes a message, and decodes in such a 
    way that it swaps case of all letters, replaces all vowels in 
    the message with the letter that appears 2 places ahead of that 
    vowel in the english alphabet. 
    Assume only letters. 
    
    Examples:
    >>> decode('TGST')
    'TEST'
    >>> decode('tHKS KS C MGSSCGG')
    'This is a message'
    
	Include these tokens in the code: def switch _ case ( ch ): if
	"""
    vowels = ['a', 'e', 'i', 'o', 'u']
    decoded_message = ''
    for letter in message:
        if letter in vowels:
            index = vowels.index(letter)
            if index < len(vowels) - 2:
                decoded_message += vowels[index + 2]
            else:
                decoded_message += vowels[index - 2]
        else:
            if letter.isupper():
                decoded_message += letter.lower()
            else:
                decoded_message += letter.upper()
    return decoded_message


if __name__ == "__main__":
    print(encode('test'))
    print(decode('TGST'))
    print(encode('This is a message'))
    print(decode('t