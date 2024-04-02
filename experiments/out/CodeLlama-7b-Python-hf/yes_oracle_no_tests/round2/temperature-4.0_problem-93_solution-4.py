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
        if ch.isupper():
            return ch.lower()
        elif ch.islower():
            return ch.upper()
        else:
            return ch

    def get_vowel(ch):
        vowels = "aeiou"
        if ch.lower() in vowels:
            return ch
        else:
            return ""

    def get_letter(ch):
        if ch.isalpha():
            return ch
        else:
            return ""

    def shift_letter(ch):
        if ch.isupper():
            return chr((ord(ch) - ord("A") + 2) % 26 + ord("A"))
        elif ch.islower():
            return chr((ord(ch) - ord("a") + 2) % 26 + ord("a"))
        else:
            return ch

    def encode_letter(ch):
        v = get_vowel(ch)
        if v == "":
            return switch_case(ch)
        else:
            return switch_case(v) + shift_letter(ch.replace(v, ""))

    return " ".join([encode_letter(ch) for ch in message])


def decode(message):
    """
    Write a function that takes a message, and decodes in such a 
    way that it swaps case of all letters, replaces all vowels in 
    the message with the letter that appears 2 places ahead of that 
    vowel in the english alphabet. 
    Assume only letters. 
    
    Examples:
    >>> decode('tgst')
    'test'
    >>> decode('tHKS KS C MGSSCGG')
    'This is a message'
    
	Include these tokens in the code: def switch _ case ( ch ): if
	"""
    # YOUR CODE HERE
    def switch_case(ch):
        if ch.isupper():
            return ch.lower()
        elif ch.islower():
            return ch.upper