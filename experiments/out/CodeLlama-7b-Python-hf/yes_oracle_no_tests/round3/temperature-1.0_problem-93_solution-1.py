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
	Do not include these tokens in the code: . is lower ():
	"""

    def switch_case(ch):
      if ch.isupper():
        return ch.lower()
      else:
        return ch.upper()

    def vowels_to_next(ch):
      if ch.lower() in 'aeiou':
        return chr(ord(ch) + 2)
      else:
        return ch

    newMessage = ''
    for ch in message:
      newMessage += switch_case(ch)
      newMessage += vowels_to_next(ch)

    return newMessage

if __name__ == '__main__':
    import doctest
    doctest.testmod()
