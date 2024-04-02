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
	Do not include these tokens in the code: . is upper ():
	"""

    def switch_case(ch):
      if ch.isupper():
        return ch.lower()
      else:
        return ch.upper()

    def replace_vowels(ch):
      if ch.lower() in ['a','e','i','o','u']:
        return chr((ord(ch)+2) % 26 + ord('a'))
      else:
        return ch

    message = list(message)
    for i in range(len(message)):
      message[i] = replace_vowels(message[i])
      message[i] = switch_case(message[i])
    return "".join(message)


def encode_v2(message):
  vowels = 'aeiou'
  for ch in message:
    if ch.lower() in vowels:
      message = message.replace(ch, chr((ord(ch) + 2) % 26))
  return message.swapcase()


if __name__ == '__main__':
    import doctest
    doctest.testmod()
