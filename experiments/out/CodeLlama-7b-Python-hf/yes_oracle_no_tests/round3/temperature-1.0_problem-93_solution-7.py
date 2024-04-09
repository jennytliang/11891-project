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
    
	Include these tokens in the code: def switch _ case
	Do not include these tokens in the code: message = message . lower ()
	"""

    # Write your code here
    vowels = {'a', 'e', 'i', 'o', 'u'}
    new_message = ''
    for letter in message:
        if letter in vowels:
            new_message += chr(ord(letter) + 2)
        elif letter.isupper():
            new_message += letter.lower()
        elif letter.islower():
            new_message += letter.upper()
        else:
            new_message += letter
    return new_message

print(encode('test'))
print(encode('This is a message'))