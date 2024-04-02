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
	Do not include these tokens in the code: # Write your code here .
	"""
    message = message.replace('a', 'b').replace('e', 'f').replace('i', 'g').replace('o', 'h').replace('u', 'i')
    message = message.replace('A', 'B').replace('E', 'F').replace('I', 'G').replace('O', 'H').replace('U', 'I')
    return message


if __name__ == '__main__':
    print(encode('test'))
    print(encode('This is a message'))
