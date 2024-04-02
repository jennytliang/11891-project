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
	Do not include these tokens in the code: == " a
	"""

    def switch_case(ch):
      if ch.islower():
        return ch.upper()
      else:
        return ch.lower()

    def encode_vowel(ch):
      if ch == 'a':
        return 'c'
      elif ch == 'e':
        return 'g'
      elif ch == 'i':
        return 'k'
      elif ch == 'o':
        return 's'
      elif ch == 'u':
        return 'w'
      else:
        return ch

    return ''.join(list(map(lambda ch: switch_case(ch) if ch.lower() in 'aeiou' else encode_vowel(ch), message)))

if __name__ == '__main__':
    import doctest
    doctest.testmod()
