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
    # YOUR CODE HERE
    vowels = "aeiouAEIOU"
    new_message = ""
    for ch in message:
        if ch in vowels:
            new_message += chr(ord(ch)+2)
        elif ch.isupper():
            new_message += ch.lower()
        else:
            new_message += ch.upper()
    return new_message

if __name__ == "__main__":
    print(encode("test"))
    print(encode("This is a message"))
