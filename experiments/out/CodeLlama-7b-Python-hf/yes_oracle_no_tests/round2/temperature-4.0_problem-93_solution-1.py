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
    
	Do not include these tokens in the code: d = {' a ':' c ',
	"""
	
	d = {'a':'c', 'e':'g', 'i':'h', 'o':'j', 'u':'n', 'A':'C',
	'E':'G', 'I':'H', 'O':'J', 'U':'N'}
	out = ""
	for char in message:
		if char in d:
			out += d[char]
		else:
			out += char
	return out

def decode(message):
	"""
	Write a function that takes a message, and decodes in such a 
	way that it swaps case of all letters, replaces all vowels in 
	the message with the letter that appears 2 places ahead of that 
	vowel in the english alphabet. 
	Assume only letters. 
    
    Examples:
    >>> decode('TGST')
    'test'
    >>> decode('tHKS KS C MGSSCGG')
    'This is a message'
	"""
	d = {'c':'a', 'g':'e', 'h':'i', 'j':'o', 'n':'u', 'C':'a',
	'G':'e', 'H':'i', 'J':'o', 'N':'u'}
	out = ""
	for char in message:
		if char in d:
			out += d[char]
		else:
			out += char
	return out

def encode_and_decode(message):
	return decode(encode(message))


def test_encode():
	assert encode("test") == "TGST"
	assert encode("This is a message") == "tHKS KS C MGSSCGG"

def test_decode():
	assert decode("TGST") == "test"
	assert decode("tHKS KS C MGSSCGG") == "This is a message"

def test_encode_and_decode():
	assert encode_and_decode("test") == "test"
	assert encode_and_decode("This is a message") == "This is a message"

test_encode()