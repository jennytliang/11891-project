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
	Do not include these tokens in the code: # Y OUR CO DE H ERE
	"""
    result = ""
    for char in message:
        if char in "aeiou":
            result += chr(ord(char) + 2)
        elif char.isupper():
            result += char.lower()
        else:
            result += char.upper()
    return result


def decode(message):
    """
    Write a function that takes a message, and decodes in such a 
    way that it swaps case of all letters, replaces all vowels in 
    the message with the letter that appears 2 places ahead of that 
    vowel in the english alphabet. 
    Assume only letters. 
    
    Examples:
    >>> decode('TGST')
    'TEST'
    >>> decode('tHKS KS C MGSSCGG')
    'This is a message'
    
	Include these tokens in the code: def switch _ case
	Do not include these tokens in the code: # Y OUR CO DE H ERE
    """
    result = ""
    for char in message:
        if char in "aeiou":
            result += chr(ord(char) - 2)
        elif char.isupper():
            result += char.lower()
        else:
            result += char.upper()
    return result


def main():
    """
    The following code is to support self-testing
    and must be included in your submitted code
    """
    assert encode("test") == "TGST"
    assert encode("This is a message") == "tHKS KS C MGSSCGG"
    assert decode("TGST") == "TEST"
    assert decode("tHKS KS C MGSSCGG") == "This is a message"
    # 
    # Tests for decode
    # 
    assert decode(encode("test")) == "test"
    assert decode(encode("This is a message")) == "This is a message"
    try:
        encode("This is 1 message")
    except Exception:
        pass
    else:
        assert False


if __name__ == "__main__":
   