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
    # pass
    encoded_message = ''
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    alpha_upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    alpha_upper_dict = {alpha_upper[i]: alpha_upper[(i + 2) % 26] for i in range(26)}
    alpha_dict = {alpha[i]: alpha[(i + 2) % 26] for i in range(26)}
    for ch in message:
        if ch in alpha:
            encoded_message += alpha_dict[ch]
        elif ch in alpha_upper:
            encoded_message += alpha_upper_dict[ch]
        else:
            encoded_message += ch
    return encoded_message

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
    
	Include these tokens in the code: def switch _ case ( ch ): if
    """
    # pass
    decoded_message = ''
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    alpha_upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    alpha_upper_dict = {alpha_upper[i]: alpha_upper[(i - 2) % 26] for i in range(26)}
    alpha_dict = {alpha[i]: alpha[(i - 2) % 26] for i in range(26)}
    for ch in message:
        if ch in alpha:
            decoded_message += alpha_dict[ch]
        elif ch in alpha_upper:
           