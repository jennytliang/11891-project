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
    
        if 'a' <= ch <= 'z':
            return chr(ord('A') + ord(ch) - ord('a'))
        elif 'A' <= ch <= 'Z':
            return chr(ord('a') + ord(ch) - ord('A'))
        else:
            return ch
    
    def swap_vowels(ch):
        if ch in 'aeiou':
            return chr(ord(ch) + 2)
        else:
            return ch
            
    def encode_message(message):
        result = ''
        for ch in message:
            result += swap_vowels(switch_case(ch))
        return result
    
    return encode_message(message)


























