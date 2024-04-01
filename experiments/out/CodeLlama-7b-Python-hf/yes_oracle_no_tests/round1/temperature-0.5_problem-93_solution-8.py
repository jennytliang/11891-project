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
    
	Include these tokens in the code:  def switch _ case ( ch ):
	Do not include these tokens in the code: pass decode message
	"""

    # encode the message
    encoded_message = ''
    for ch in message:
        if ch in 'aeiou':
            encoded_message += chr(ord(ch) + 2)
        elif ch.isupper():
            encoded_message += ch.lower()
        else:
            encoded_message += ch.upper()
    return encoded_message


if __name__ == '__main__':
    message = input('Enter a message to encode: ')
    print(f'Encoded message: {encode(message)}')
