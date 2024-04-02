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
    vowels = 'aeiou'
    message = message.lower()
    encoded_message = ''

    for ch in message:
        if ch in vowels:
            encoded_message += chr((ord(ch) + 2 - ord('a')) % 26 + ord('a'))
        else:
            encoded_message += ch.swapcase()

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
    vowels = 'aeiou'
    message = message.lower()
    decoded_message = ''

    for ch in message:
        if ch in vowels:
            decoded_message += chr((ord(ch) - 2 - ord('a')) % 26 + ord('a'))
        else:
            decoded_message += ch.swapcase()

    return decoded_message


def main():
    message = input('Input a message: ')

    print(message, '->', encode(message))
    print(message, '->', decode(encode(message)))


if __name__ == '__main__':
    main()
