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
    
	Include these tokens in the code: ord (" A ") <= ord ( ch ) <=
	"""


    def switch_case(ch):
    	if ch.islower():
    		return ch.upper()
    	else:
    		return ch.lower()
    
    def swap_vowels(ch):
    	if ch in ['a', 'e', 'i', 'o', 'u']:
    		return chr((ord(ch) + 2) % 26 + ord('a'))
    	else:
    		return ch
    
    def encode_letters(ch):
    	return switch_case(swap_vowels(ch))
    
    return ''.join(map(encode_letters, message))


def decode(message):
    """
    Write a function that takes a message, and encodes in such a 
    way that it swaps case of all letters, replaces all vowels in 
    the message with the letter that appears 2 places ahead of that 
    vowel in the english alphabet. 
    Assume only letters. 
    
    Examples:
    >>> decode('TGST')
    'test'
    >>> decode('tHKS KS C MGSSCGG')
    'This is a message'
    
	Include these tokens in the code: ord (" A ") <= ord ( ch ) <=
	"""

    def decode_letters(ch):
    	return switch_case(swap_vowels(ch))
    
    return ''.join(map(decode_letters, message))


if __name__ == '__main__':
    import doctest
    doctest.testmod()
