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
    
	Include these tokens in the code: def switch _ case
	Do not include these tokens in the code: # Your code here message
	"""

    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    new_message = ''
    for letter in message:
        if letter in vowels:
            if letter in vowels[0:5]:
                new_message += vowels[vowels.index(letter) + 2]
            else:
                new_message += vowels[vowels.index(letter) - 2]
        else:
            if letter.isupper():
                new_message += letter.lower()
            else:
                new_message += letter.upper()
    return new_message


if __name__ == '__main__':
    import doctest
    doctest.testmod()
