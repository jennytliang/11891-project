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
    result = ""
    for ch in message:
        if ch.isalpha():
            if ch.islower():
                result += ch.upper()
            elif ch.isupper():
                result += ch.lower()
            else:
                result += ch
        else:
            result += ch
    for i in range(len(result)):
        if result[i].lower() in "aeiou":
            result = result[:i] + chr(ord(result[i].lower()) + 2) + result[i + 1:]
    return result


def decode(message):
    """
    Write a function that takes a message, and decodes it by 
    reversing the steps that were taken in the encode function. 
    
    Examples:
    >>> decode('TGST')
    'test'
    >>> decode('tHKS KS C MGSSCGG')
    'This is a message'
    """
    result = ""
    for ch in message:
        if ch.isalpha():
            if ch.islower():
                result += ch.upper()
            elif ch.isupper():
                result += ch.lower()
            else:
                result += ch
        else:
            result += ch
    for i in range(len(result)):
        if result[i].lower() in "aeiou":
            result = result[:i] + chr(ord(result[i].lower()) - 2) + result[i + 1:]
    return result
