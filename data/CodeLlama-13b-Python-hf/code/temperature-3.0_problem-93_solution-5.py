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
    """
    message = list(message)
    
    for idx, letter in enumerate(message):
        if letter == 'A':
            message[idx] = 'C'
        if letter == 'a':
            message[idx] = 'c'
        if letter == 'E':
            message[idx] = 'G'
        if letter == 'e':
            message[idx] = 'g'
        if letter == 'I':
            message[idx] = 'J'
        if letter == 'i':
            message[idx] = 'j'
        if letter == 'O':
            message[idx] = 'Q'
        if letter == 'o':
            message[idx] = 'q'
        if letter == 'U':
            message[idx] = 'W'
        if letter == 'u':
            message[idx] = 'w'
        if letter == 'Y':
            message[idx] = 'A'
        if letter == 'y':
            message[idx] = 'a'
    
    result = ''
    
    for letter in message:
        if letter.isupper():
            result += chr(ord(letter) + 2)
        else:
            result += letter
    
    return result

