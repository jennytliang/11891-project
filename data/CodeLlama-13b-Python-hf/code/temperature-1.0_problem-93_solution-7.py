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
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    message = list(message)
    for i in range(len(message)):
        if message[i] in vowels:
            message[i] = chr(ord(message[i]) + 2)
        if message[i].isupper():
            message[i] = message[i].lower()
        else:
            message[i] = message[i].upper()
    return ''.join(message)