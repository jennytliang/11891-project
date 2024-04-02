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
	Do not include these tokens in the code: result = "" for
	"""
    vowels = ['A','E','I','O','U']
    result = ""
    for i in range(len(message)):
        ch = message[i]
        if ch in vowels:
            result += chr(ord(message[i]) + 2)
        elif ord(ch) > ord('Z'):
            result += chr(ord(ch) - 26)
        else:
            result += ch
    return result
    
if __name__ == '__main__':
    import doctest
    doctest.testmod()
