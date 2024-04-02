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
    encodedMessage = ""    
    i = 2
    for char in message:
       # char.lower () 
        if char.islower():
            encodedMessage += char.upper ()  ;
        elif char.isupper():
            encodedMessage += char.lower ()  ;
        elif char.isdigit ():
            encodedMessage += int (char) + i  ;
        elif char.isspace ():
            encodedMessage += char           ; 
        i += 2
    return encodedMessage
   
message = input ("Enter the message: ")

print (encode(message))