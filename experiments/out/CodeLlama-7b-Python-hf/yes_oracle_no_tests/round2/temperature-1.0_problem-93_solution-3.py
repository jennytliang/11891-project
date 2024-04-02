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
	Do not include these tokens in the code: == ' a ' or == ' e
	"""

    def switch_case(ch):
      if 'A' <= ch <= 'Z':
        return chr(ord(ch) + 32)
      elif 'a' <= ch <= 'z':
        return chr(ord(ch) - 32)
      else:
        return ch

    def replace_vowel(ch):
      if ch in 'aeiou':
        return chr(ord(ch) + 2)
      else:
        return ch

    encoded_message = ''
    for ch in message:
      encoded_message += switch_case(ch)
      encoded_message += replace_vowel(ch)
    return encoded_message

def decode(message):
    """
    Write a function that takes in an encoded message, and decodes it. 
    """

    def switch_case(ch):
      if 'A' <= ch <= 'Z':
        return chr(ord(ch) - 32)
      elif 'a' <= ch <= 'z':
        return chr(ord(ch) + 32)
      else:
        return ch

    def replace_vowel(ch):
      if ch in 'aeiou':
        return chr(ord(ch) - 2)
      else:
        return ch

    decoded_message = ''
    for ch in message:
      decoded_message += switch_case(ch)
      decoded_message += replace_vowel(ch)
    return decoded_message


if __name__ == "__main__":
    print(encode('test'))
    print(encode('This is a message'))
    print(decode('tHKS KS C MGSSCGG'))