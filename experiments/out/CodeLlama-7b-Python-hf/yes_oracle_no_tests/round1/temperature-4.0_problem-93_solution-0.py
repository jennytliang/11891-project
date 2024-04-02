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

    def switch(c):
        return c.upper() if c.islower() else c.lower()

    d = {
        "a": "c",
        "e": "g",
        "i": "k",
        "o": "n",
        "u": "m",
        "b": "f",
        "c": "d",
        "d": "e",
        "f": "b",
        "g": "a",
        "h": "l",
        "j": "p",
        "k": "i",
        "l": "h",
        "m": "n",
        "n": "m",
        "p": "j",
        "q": "v",
        "r": "o",
        "s": "r",
        "t": "q",
        "v": "q",
        "w": "s",
        "x": "w",
        "y": "t",
        "z": "u",
    }

    new_message = "".join(d.get(c, c) if c.lower() in d else c for c in message)

    return "".join(switch(c) for c in new_message)


if __name__ == "__main__":
    print(encode("test"))
    print(encode("This is a message"))
