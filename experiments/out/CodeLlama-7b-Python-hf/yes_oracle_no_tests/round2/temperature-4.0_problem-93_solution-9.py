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
	Do not include these tokens in the code: # code goes here new
	"""
    #code goes here
    new_message = ''
    vowels = 'aeiou'
    for letter in message:
        if letter.lower() in vowels:
            new_message += switch(letter)
        else:
            new_message += switch(letter)
    return new_message

def switch(letter):
    if letter.islower():
        if letter == 'a':
            return 'c'
        elif letter == 'e':
            return 'g'
        elif letter == 'i':
            return 'k'
        elif letter == 'o':
            return 't'
        elif letter == 'u':
            return 'w'
        elif letter == 'y':
            return 'p'
        else:
            return letter.upper()
    else:
        if letter == 'C':
            return 'A'
        elif letter == 'G':
            return 'E'
        elif letter == 'K':
            return 'I'
        elif letter == 'T':
            return 'O'
        elif letter == 'W':
            return 'U'
        elif letter == 'P':
            return 'Y'
        else:
            return letter.lower()

if __name__ == '__main__':
    print(encode('test'))
    print(encode('This is a message'))
