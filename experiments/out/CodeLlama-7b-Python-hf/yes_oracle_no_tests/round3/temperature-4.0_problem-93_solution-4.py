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
    #pass
    # replace vowels with the letter that appears 2 places ahead of that vowel in the english alphabet
    # case swap all letters
    # YOUR CODE HERE
    # create a dictionary of vowels and their shifted counterparts
    vowels = {'a': 'c', 'e': 'g', 'i': 'k', 'o': 's', 'u': 'v', 'y': 'b'}
    # create a list of all the letters in the message
    message_list = list(message)
    # loop through the message
    for i in range(len(message_list)):
        # check if the current letter in the message is in the vowels dictionary
        if message_list[i] in vowels:
            # if it is in the dictionary, replace the letter with the value in the dictionary
            message_list[i] = vowels[message_list[i]]
        # if the current letter is in the list of uppercase letters, swap the case
        if message_list[i].isupper():
            # if it is uppercase, swap the case
            message_list[i] = message_list[i].swapcase()
    # join the message into a string
    message = ''.join(message_list)
    # return the encoded message
    return message


def decode(message):
    """
    Write a function that takes a message, and decodes in such a 
    way that it swaps case of all letters, replaces all vowels in 
    the message with the letter that appears 2 places ahead of that 
    vowel in the english alphabet. 
    Assume only letters. 
    
    Examples:
    >>> decode('TGST')
    'test'
    >>> decode('tHKS KS C MGSSCGG')
    'This is a message'
    
	Do not include these tokens in the code: # Y OUR CO DE H ERE
	"""
    #pass
    # replace vowels with the letter that appears 2 places ahead of that vowel in the english alphabet
    # case swap all letters
   