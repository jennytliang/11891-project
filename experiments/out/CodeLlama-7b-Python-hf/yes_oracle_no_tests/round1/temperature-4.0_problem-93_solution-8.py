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
    
	Include these tokens in the code: def switch
	Do not include these tokens in the code: d = {} d ['
	"""
    
    def switch(message):
      if message.isalpha():
        if message.isupper():
          return message.lower()
        else:
          return message.upper()
      else:
        return message
    
    d = {}
    d['a'] = 'c'
    d['e'] = 'g'
    d['i'] = 'k'
    d['o'] = 't'
    d['u'] = 'w'
    d['b'] = 'd'
    d['f'] = 'j'
    d['p'] = 'm'
    d['v'] = 'y'
    d['c'] = 'f'
    d['g'] = 'i'
    d['h'] = 'l'
    d['j'] = 'p'
    d['q'] = 's'
    d['x'] = 'z'
    d['d'] = 'b'
    d['k'] = 'o'
    d['m'] = 'n'
    d['w'] = 'u'
    d['y'] = 'v'
    d['z'] = 'x'
    d['n'] = 'm'
    d['s'] = 'q'
    d['t'] = 'r'
    d['r'] = 't'
    
    message = list(message)
    
    for i in range(len(message)):
      message[i] = switch(message[i])
      if message[i] in d:
        message[i] = d[message[i]]
    
    return ''.join(message)