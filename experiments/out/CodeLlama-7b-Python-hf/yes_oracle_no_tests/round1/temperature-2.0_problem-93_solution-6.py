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

    message = message.lower()
    message = message.replace(' ', '')
    new_message = ''
    for ch in message:
        if ch == 'a':
            new_message += 'D'
        elif ch == 'e':
            new_message += 'F'
        elif ch == 'i':
            new_message += 'H'
        elif ch == 'o':
            new_message += 'J'
        elif ch == 'u':
            new_message += 'L'
        elif ch == 'y':
            new_message += 'A'
        elif ch == 'b':
            new_message += 'E'
        elif ch == 'c':
            new_message += 'G'
        elif ch == 'd':
            new_message += 'I'
        elif ch == 'f':
            new_message += 'K'
        elif ch == 'g':
            new_message += 'M'
        elif ch == 'h':
            new_message += 'O'
        elif ch == 'j':
            new_message += 'T'
        elif ch == 'k':
            new_message += 'W'
        elif ch == 'l':
            new_message += 'B'
        elif ch == 'm':
            new_message += 'N'
        elif ch == 'n':
            new_message += 'P'
        elif ch == 'p':
            new_message += 'V'
        elif ch == 'q':
            new_message += 'X'
        elif ch == 'r':
            new_message += 'Y'
        elif ch == 's':
            new_message += 'Z'
        elif ch == 't':
            new_message += 'C'
        elif ch == 'u':
            new_message += 'D'
        elif ch == 'v':
            new_message += 'E'
        elif ch == 'w':
            new_message += 'F'
        elif ch == 'x':
            new_message += 'G'
        elif ch == 'y':
            new_message += 'H'
        elif ch == 'z':
