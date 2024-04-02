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
    
	Include these tokens in the code: def
	Do not include these tokens in the code: result = "" letters =
	"""
    
    dictionary = {"A":"B","B":"A","C":"D","D":"C","E":"F","F":"E","G":"H","H":"G","I":"J",
    "J":"I","K":"L","L":"K","M":"N","N":"M","O":"P","P":"O","Q":"R","R":"Q","S":"T",
    "T":"S","U":"V","V":"U","W":"X","X":"W","Y":"Z","Z":"Y"}  
    result = ""
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
    for index in range(0,len(message)):
        if message[index] not in letters:
            result += message[index]
        if message[index] in dictionary.keys():
            result += dictionary[message[index]]
        if message[index] in letters:
            c = (ord(message[index]) + 2) % 26
            if c <10:
                result += chr(c+55)
            if c >= 10: 
                result += chr(c+79)
            
    return result
    
def encode2(message):
    """
    Write a function that takes a message, and encodes in such a 
    way that it swaps case of all letters, replaces all vowels in 
    the message with the letter that appears 2 places ahead of that 
    vowel in the english alphabet. 
    Assume only letters. 
    
    Examples:
    >>> encode2('test')
    'TGST'
    >>> encode2('This is a message')
    'tHKS KS C MGSSCGG'
    
	Include these tokens in the code: def
	Do not include these tokens in the code: result = ""
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    """
    
    result = ""
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    code = ["B","A","D","