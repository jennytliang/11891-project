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
    # YOUR CODE HERE
    message = message.replace('a', 'B')
    message = message.replace('e', 'D')
    message = message.replace('i', 'F')
    message = message.replace('o', 'G')
    message = message.replace('u', 'H')
    message = message.replace('A', 'b')
    message = message.replace('E', 'd')
    message = message.replace('I', 'f')
    message = message.replace('O', 'g')
    message = message.replace('U', 'h')
    message = message.upper()
    message = message.replace('B', 'A')
    message = message.replace('D', 'E')
    message = message.replace('F', 'I')
    message = message.replace('G', 'O')
    message = message.replace('H', 'U')
    return message


def encode_2(message):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for letter in message:
        if letter in vowels:
            num = vowels.index(letter)
            result.append(vowels[num+2])
        else:
            result.append(letter.upper() if letter.islower() else letter)
    return ''.join(result)


if __name__ == '__main__':
    import doctest
    doctest.testmod()
