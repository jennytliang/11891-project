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
	Do not include these tokens in the code: d = {} d ['
	"""
    message = message.lower()
    message = message.replace(" ", "")
    new_message = ""
    for letter in message:
        if letter in "aeiou":
            new_message += "cdefghijklmnopqrstuvwxyz"[ord(letter) - 97 + 2]
        else:
            new_message += letter.upper()
    return new_message
