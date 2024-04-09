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
    encoded_message = ""
    for ch in message:
        if ch.isalpha():
            if ch.isupper():
                ch = ch.lower()
            elif ch.islower():
                ch = ch.upper()
            if ch in "aeiou":
                ch = chr(ord(ch) + 2)
        encoded_message += ch
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
    'test'
    >>> decode('tHKS KS C MGSSCGG')
    'This is a message'
    
	Include these tokens in the code: def switch _ case ( ch ): if
	"""
    decoded_message = ""
    for ch in message:
        if ch.isalpha():
            if ch.isupper():
                ch = ch.lower()
            elif ch.islower():
                ch = ch.upper()
            if ch in "aeiou":
                ch = chr(ord(ch) - 2)
        decoded_message += ch
    return decoded_message


def main():
    message = "This is a message"
    print(encode(message))
    print(decode(encode(message)))


if __name__ == "__main__":
    main()
