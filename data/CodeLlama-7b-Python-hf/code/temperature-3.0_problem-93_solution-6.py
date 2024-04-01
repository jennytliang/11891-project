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
    result = ''
    
    for char in message:
        if char.isalpha():
            if char.isupper():
                result += char.lower()
            else:
                if char == 'a':
                    result += 'C'
                elif char == 'e':
                    result += 'G'
                elif char == 'i':
                    result += 'B'
                elif char == 'o':
                    result += 'P'
                elif char == 'u':
                    result += 'M'
                else:
                    result += str(chr(ord(char) + 2))
        else:
            result += char
    
    return result
                