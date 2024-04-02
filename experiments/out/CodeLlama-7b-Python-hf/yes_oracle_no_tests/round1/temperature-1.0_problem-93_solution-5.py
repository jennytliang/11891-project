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
    
	Include these tokens in the code: def switch _ case ( ch ): if
	"""
    encoded = ''
    vowels = 'aeiouAEIOU'
    for ch in message:
        if ch == ' ':
            encoded += ch
        elif ch in vowels:
            if ch == ch.lower():
                ch = chr(ord(ch.upper())-2)
            else:
                ch = chr(ord(ch.lower())-2)
        encoded += ch.upper() if ch.isupper() else ch.lower()
    return encoded


"""
def encode(message):
    encoded = ''
    for ch in message:
        if ch in 'aeiou':
           ch = chr(ord(ch.upper()) - 2)
        if ch.islower():
            ch = ch.upper()
        encoded += chr(ord(ch) - 2)
    return encoded
"""

print(encode("hi"))
print(encode("test"))
print(encode('This is a message'))
print(encode('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'))
