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

    message = message.replace('a', 'A').\
        replace('e', 'E').replace('i', 'I').replace('o', 'O').replace('u', 'U').\
        replace('A', 'a').replace('E', 'e').replace('I', 'i').replace('O', 'o').replace('U', 'u')
    return ''.join(list(map(lambda x: ord(x) - 2 % 26 + 97 if x in "aeiouAEIOU" else ord(x) + 1 % 26 + 97 if x.isalpha() else x, message)))


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
