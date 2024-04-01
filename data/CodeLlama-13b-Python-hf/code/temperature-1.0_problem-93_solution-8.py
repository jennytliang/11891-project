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
    new_message = ''
    for letter in message:
        if letter in vowels:
            new_message += vowels[(vowels.index(letter) + 2) % len(vowels)]
        else:
            new_message += letter.lower() if letter.isupper() else letter.upper()
    return new_message