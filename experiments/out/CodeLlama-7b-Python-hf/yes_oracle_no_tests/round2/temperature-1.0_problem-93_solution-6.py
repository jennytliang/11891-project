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
    
	Include these tokens in the code: def switch _ case ( ch ):
	Do not include these tokens in the code: message = message . replace ('
	"""
    
    message = message.casefold()
    alpha = list("abcdefghijklmnopqrstwxyz")
    alpha2 = list("cdefghijklmnopqrstwxyzab")
    
    listMessage=list(message)
    i=0
    def listReplace(value):
        x=alpha2.index(alpha.index(value))
        global i 
        i =(i + x)%26
        return(alpha[i])
        
    for j, value in enumerate(listMessage):
        if value in alpha:
            listMessage[j]=listReplace(value)
    return ''.join(str(x) for x in listMessage)

if __name__ == "__main__":
    print(encode(""))
    print(encode('test'))
    print(encode('This is a message'))
    


    
    