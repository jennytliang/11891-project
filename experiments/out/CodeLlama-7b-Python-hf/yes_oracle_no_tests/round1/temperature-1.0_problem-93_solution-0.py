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
    def switch_case(ch):
        if ch.islower():
            return ch.upper()
        else:
            return ch.lower()

    def vowel_replace(ch):
        vowels = "aeiou"
        if ch.lower() in vowels:
            return chr(ord(ch) + 2)
        else:
            return ch

    return "".join(map(vowel_replace, map(switch_case, message)))


def encode_2(message):
    return "".join(
        chr(ord(c) + (2 if c in "aeiou" else 0) + (1 if c.islower() else -1))
        for c in message
    )


def encode_3(message):
    return "".join(
        chr(ord(c) + (2 if c in "aeiou" else 0) + (1 if c.islower() else -1))
        for c in message
    )


def encode_4(message):
    return "".join(
        chr(ord(c) + (2 if c in "aeiou" else 0) + (1 if c.islower() else -1))
        for c in message
    )


def encode_5(message):
    return "".join(
        chr(ord(c) + (2 if c in "aeiou" else 0) + (1 if c.islower() else -1))
        for c in message
    )


def encode_6(message):
    return "".join(
        chr(ord(c) + (2 if c in "aeiou" else 0) + (1 if c.islower() else -1))
        for c in message
    )


def encode_7(message):
    return "".join(
        chr(ord(c) + (2 if c in "aeiou" else 0) + (1 if c.islower() else -1))
        for c in message
    )


if __name__