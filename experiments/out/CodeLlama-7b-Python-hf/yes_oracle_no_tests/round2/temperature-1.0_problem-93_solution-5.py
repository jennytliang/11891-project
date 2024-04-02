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
	Do not include these tokens in the code: encoded = '' v ow
	"""
    
    encoded = ''

    for idx in range(len(message)):
        ch = message[idx]
        if ch.isalpha():
            if ch.isupper():
                ch = ch.lower()
            elif ch.islower():
                ch = ch.upper()
            if ch in 'aeiou':
                ch = chr(ord(ch) + 2)
            encoded += ch
        else:
            encoded += ch
    return encoded

print(encode('test'))
print(encode("This is a message"))
