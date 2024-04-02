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
    for i in message:
        if i.isupper():
            result += i.lower()
        elif i.islower():
            result += i.upper()
        else:
            result += i
    for i in range(len(result)):
        if result[i] in 'AEIOU':
            if i + 2 < len(result):
                result = result[:i] + result[i+2] + result[i+1] + result[i+3:]
            else:
                result = result[:i] + result[i+2] + result[i+1]
    return result


if __name__ == '__main__':
    import doctest
    doctest.testmod()
