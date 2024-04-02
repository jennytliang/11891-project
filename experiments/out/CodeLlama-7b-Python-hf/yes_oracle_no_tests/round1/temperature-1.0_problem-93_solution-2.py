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

    # Use built-in function lower () to ensure all letters are
    # converted to lowercase, then use lowercase
    # message to create our result
    result = ""
    VOWELS = "aeiou"

    for char in message.lower():

        if char in VOWELS:
            char = chr(ord(char) + 2)
            result += char
        elif char.isupper():
            char = char.swapcase()
            result += char
        else:
            result += char

    print(result) # display function result
    return result


encode("Test")
encode("I love Python")
encode("There is nothing else to say")