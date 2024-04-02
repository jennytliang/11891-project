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
    res = ""
    for i in message:
        if i.isupper():
            res += i.lower()
        elif i.islower():
            res += i.upper()
        elif i in "aeiou":
            res += chr(ord(i)+2)
        else:
            res += i
    return res

if __name__ == "__main__":
    import doctest
    doctest.testmod()
