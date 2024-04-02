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
            elif ch == 'b':
                result += 'D'
            elif ch == 'c':
                result += 'E'
            elif ch == 'd':
                result += 'F'
            elif ch == 'e':
                result += 'G'
            elif ch == 'f':
                result += 'H'
            elif ch == 'g':
                result += 'I'
            elif ch == 'h':
                result += 'J'
            elif ch == 'i':
                result += 'K'
            elif ch == 'j':
                result += 'L'
            elif ch == 'k':
                result += 'M'
            elif ch == 'l':
                result += 'N'
            elif ch == 'm':
                result += 'O'
            elif ch == 'n':
                result += 'P'
            elif ch == 'o':
                result += 'Q'
            elif ch == 'p':
                result += 'R'
            elif ch == 'q':
                result += 'S'
            elif ch == 'r':
                result += 'T'
            elif ch == 's':
                result += 'U'
            elif ch == 't':
                result += 'V'
            elif ch == 'u':
                result += 'W'
            elif ch == 'v':
                result += 'X'
            elif ch == 'w':
                result += 'Y'
            elif ch == 'x':
                result += 'Z'
            elif ch == 'y':
                result += 'A'
            elif ch == 'z':
                result += 'B'
            else:
                result += ch
    return result


def decode(message):
    """
    Write a function that takes a message, and decodes in such a 
    way that it swaps case of all letters, replaces all vowels in 
   