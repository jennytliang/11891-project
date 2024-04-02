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
    #code goes here
    new_message = []
    for letter in message:
        if letter.isalpha():
            if letter.isupper():
                new_message.append(letter.lower())
            elif letter.islower():
                new_message.append(letter.upper())
            else:
                new_message.append(letter)
        else:
            new_message.append(letter)
    new_message = ''.join(new_message)
    new_message = list(new_message)
    for i in range(len(new_message)):
        if new_message[i] in 'AEIOU':
            new_message[i] = chr(ord(new_message[i]) + 2)
    new_message = ''.join(new_message)
    return new_message
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    