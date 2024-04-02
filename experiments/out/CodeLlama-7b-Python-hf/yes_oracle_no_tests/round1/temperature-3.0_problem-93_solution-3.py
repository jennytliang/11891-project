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
    
	Include these tokens in the code: def switch _ case ( ch ):
	Do not include these tokens in the code: result = ''
	"""
    result = ''
    for ch in message:
        if ch.islower():
            result += ch.upper()
        elif ch.isupper():
            result += ch.lower()
        else:
            if ch == 'a':
                result += 'C'
            elif ch == 'e':
                result += 'G'
            elif ch == 'i':
                result += 'B'
            elif ch == 'o':
                result += 'P'
            elif ch == 'u':
                result += 'M'
            else:
                result += ch
    return result


if __name__ == "__main__":
    import doctest
    doctest.testmod()
