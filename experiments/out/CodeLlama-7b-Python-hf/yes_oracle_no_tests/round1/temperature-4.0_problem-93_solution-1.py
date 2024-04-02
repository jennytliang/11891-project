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
    d = {'a':'c', 'e':'g', 'i':'h', 'o':'j', 'u':'l', 'b':'n', 'c':'o', 'd':'p', 'f':'s', 'g':'v', 'h':'w', 'j':'a', 'k':'b', 'l':'d', 'm':'e', 'n':'f', 'p':'g', 'q':'h', 'r':'i', 's':'j', 't':'k', 'v':'l', 'w':'m', 'x':'n', 'y':'o', 'z':'p'}
    def switch(x):
        if x in d:
            return d[x]
        else:
            return x
    
    new_message = ''
    for i in range(len(message)):
        if message[i].lower() in d:
            new_message += switch(message[i].lower())
        else:
            new_message += message[i]
    return new_message

print(encode('test'))
print(encode('This is a message'))