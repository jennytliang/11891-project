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
    
	Include these tokens in the code: def switch
	Do not include these tokens in the code: v ow els = [' a
	"""
    # YOUR CODE HERE
    message = message.lower()
    new_message = ''
    for letter in message:
        new_message += switch(letter)
    return new_message

def switch(letter):
    if letter == 'a':
        return 'f'
    if letter == 'b':
        return 'g'
    if letter == 'c':
        return 'h'
    if letter == 'd':
        return 'i'
    if letter == 'e':
        return 'j'
    if letter == 'f':
        return 'k'
    if letter == 'g':
        return 'l'
    if letter == 'h':
        return 'm'
    if letter == 'i':
        return 'n'
    if letter == 'j':
        return 'o'
    if letter == 'k':
        return 'p'
    if letter == 'l':
        return 'q'
    if letter == 'm':
        return 'r'
    if letter == 'n':
        return 's'
    if letter == 'o':
        return 't'
    if letter == 'p':
        return 'u'
    if letter == 'q':
        return 'v'
    if letter == 'r':
        return 'w'
    if letter == 's':
        return 'x'
    if letter == 't':
        return 'y'
    if letter == 'u':
        return 'z'
    if letter == 'v':
        return 'a'
    if letter == 'w':
        return 'b'
    if letter == 'x':
        return 'c'
    if letter == 'y':
        return 'd'
    if letter == 'z':
        return 'e'
    else:
        return letter.upper()

if __name__ == '__main__':
    import doctest
    doctest.testmod()
