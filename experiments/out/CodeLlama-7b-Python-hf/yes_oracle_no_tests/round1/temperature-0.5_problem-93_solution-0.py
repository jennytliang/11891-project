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
    
	Include these tokens in the code:  def switch _ case ( ch ):
	Do not include these tokens in the code: pass decode message
	"""

    # Your code here
    letters = "abcdefghijklmnopqrstuvwxyz"
    vowels = "aeiou"
    encoded = ""
    for ch in message:
        if ch.lower() in vowels:
            position = letters.index(ch.lower())
            encoded += letters[position + 2]
        else:
            encoded += ch.upper() if ch.isalpha() else ch
    return encoded


def decode(message):
    """
    Write a function that takes a message, and decodes the message from 
    the encoding created in the last exercise. 
    Assume only letters. 
    
    Examples:
    >>> decode('TGST')
    'test'
    >>> decode('tHKS KS C MGSSCGG')
    'This is a message'
    """
    letters = "abcdefghijklmnopqrstuvwxyz"
    vowels = "aeiou"
    decoded = ""
    for ch in message:
        if ch.lower() in vowels:
            position = letters.index(ch.lower())
            decoded += letters[position - 2]
        else:
            decoded += ch.upper() if ch.isalpha() else ch
    return decoded


if __name__ == '__main__':
    import doctest
    doctest.testmod()
