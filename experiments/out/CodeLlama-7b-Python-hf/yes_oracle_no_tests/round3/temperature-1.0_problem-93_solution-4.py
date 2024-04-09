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
	Do not include these tokens in the code: v ow els = " ae i
	"""
    # YOUR CODE HERE
    def switch_case(char):
        if char.islower():
            return char.upper()
        elif char.isupper():
            return char.lower()
        else:
            return char

    def vowels(char):
        vowels = 'aeiou'
        return vowels.find(char.lower())

    def encode_string(message):
        return "".join([switch_case(char) if vowels(char) != -1 else message[vowels(char):vowels(char) + 2] for char in message])
    return encode_string(message)


def encode_v2(message):
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
	Do not include these tokens in the code: v ow els = " ae i
	"""
    # YOUR CODE HERE
    def switch_case(char):
        if char.islower():
            return char.upper()
        elif char.isupper():
            return char.lower()
        else:
            return char

    def vowels(char):
        vowels = 'aeiou'
        return vowels.find(char.lower())

    def encode_string(message):
        return "".join([switch_case(char) if vowels(char) != -1 else message[vowels(char):vowels(char) + 2] for char in message])
    return encode_string(message)


def encode_v3(message):
    """
    Write a function that