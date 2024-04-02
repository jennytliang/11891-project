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
    def switch_case(ch):
        if ch.isupper():
            return ch.lower()
        if ch.islower():
            return ch.upper()
        return ch

    return "".join(
        [
            switch_case(ch)
            if ch in "aeiou"
            else switch_case(chr(ord(ch) + 2 if ord(ch) <= ord("z") else ord(ch) - 26))
            for ch in message
        ]
    )


if __name__ == "__main__":
    print(encode("test"))
    print(encode("This is a message"))
