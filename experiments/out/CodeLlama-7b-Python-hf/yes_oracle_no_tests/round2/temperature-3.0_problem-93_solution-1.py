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
	Do not include these tokens in the code: # write your code here
	"""
    # write your code here
    def switch_case(ch):
        if ch.isupper():
            return ch.lower()
        else:
            return ch.upper()

    message = message.replace('a', '*').replace('e', '*').replace('i', '*') \
        .replace('o', '*').replace('u', '*').replace('A', '*').replace('E', '*') \
        .replace('I', '*').replace('O', '*').replace('U', '*')
    message = message.split('*')
    res = ''
    i = 0
    while i < len(message):
        if i == len(message) - 1:
            res += message[i]
        else:
            res += message[i] + message[i + 1]
            i += 2
    res = res.replace('*', '').replace('x', '').replace('X', '')
    return res


def decode(message):
    """
    Write a function that takes a message, and encodes in such a 
    way that it swaps case of all letters, replaces all vowels in 
    the message with the letter that appears 2 places ahead of that 
    vowel in the english alphabet. 
    Assume only letters. 
    
    Examples:
    >>> decode('TGST')
    'test'
    >>> decode('tHKS KS C MGSSCGG')
    'This is a message'
    
	Include these tokens in the code: def switch _ case ( ch ):
	Do not include these tokens in the code: # write your code here
	"""
    # write your code here
    def switch_case(ch):
        if ch.isupper():
            return ch.lower()
        else:
            return ch.upper()

    message = message.replace('a', '*').replace('e', '*').replace('i', '*') \
        .replace('o', '*').replace('u', '*').replace('A', '*').replace('E', '*') \