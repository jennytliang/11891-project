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
    # Your code here
    message = message.lower()
    encoding = ''
    for i in range(len(message)):
        if message[i] == 'a':
            encoding += 'D'
        elif message[i] == 'e':
            encoding += 'F'
        elif message[i] == 'i':
            encoding += 'H'
        elif message[i] == 'o':
            encoding += 'J'
        elif message[i] == 'u':
            encoding += 'N'
        elif message[i] == ' ':
            encoding += ' '
        elif message[i] == 'b':
            encoding += 'Q'
        elif message[i] == 'c':
            encoding += 'P'
        elif message[i] == 'd':
            encoding += 'R'
        elif message[i] == 'f':
            encoding += 'T'
        elif message[i] == 'g':
            encoding += 'S'
        elif message[i] == 'h':
            encoding += 'U'
        elif message[i] == 'j':
            encoding += 'V'
        elif message[i] == 'k':
            encoding += 'W'
        elif message[i] == 'l':
            encoding += 'X'
        elif message[i] == 'm':
            encoding += 'Y'
        elif message[i] == 'n':
            encoding += 'Z'
        elif message[i] == 'p':
            encoding += 'B'
        elif message[i] == 'q':
            encoding += 'C'
        elif message[i] == 'r':
            encoding += 'D'
        elif message[i] == 's':
            encoding += 'E'
        elif message[i] == 't':
            encoding += 'F'
        elif message[i] == 'v':
            encoding += 'J'
        elif message[i] == 'w':
            encoding += 'K'
        elif message[i] == 'x':
            encoding += 'L'
        elif message[i] == 'y':
            encoding += 'M'
        elif message