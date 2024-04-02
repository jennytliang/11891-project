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
    # YOUR CODE HERE
    vowels = 'aeiou'
    message = message.lower()
    result = ''
    for c in message:
        if c in vowels:
            i = vowels.find(c)
            result += vowels[(i + 2) % len(vowels)]
        else:
            if c.isalpha():
                result += c.upper() if c.isupper() else c.lower()
            else:
                result += c
    return result


if __name__ == "__main__":
    print(encode("test"))
    print(encode("This is a message"))