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
    
	Do not include these tokens in the code: # Y OUR CO DE H ERE
	"""
    # YOUR CODE HERE
    # pass
    message = message.replace('a', 'A')
    message = message.replace('e', 'E')
    message = message.replace('i', 'I')
    message = message.replace('o', 'O')
    message = message.replace('u', 'U')
    message = message.replace('A', 'a')
    message = message.replace('E', 'e')
    message = message.replace('I', 'i')
    message = message.replace('O', 'o')
    message = message.replace('U', 'u')
    message = message.replace(' ', ' ')
    message = message.replace('1', '1')
    message = message.replace('0', '0')
    message = message.replace('7', '7')
    message = message.replace('8', '8')
    message = message.replace('3', '3')
    message = message.replace('9', '9')
    message = message.replace('4', '4')
    message = message.replace('5', '5')
    message = message.replace('6', '6')
    message = message.replace('2', '2')
    message = message.replace('-', '-')
    message = message.replace('_', '_')
    message = message.replace('=', '=')
    message = message.replace('+', '+')
    message = message.replace('*', '*')
    message = message.replace('@', '@')
    message = message.replace('$', '$')
    message = message.replace('%', '%')
    message = message.replace('^', '^')
    message = message.replace('&', '&')
    message = message.replace('(', '(')
    message = message.replace(')', ')')
    message = message.replace('[', '[')
    message = message.replace(']', ']')
    message = message.replace('{', '{')
    message = message.replace('}', '}')
    message = message.replace('<', '<')
    message = message