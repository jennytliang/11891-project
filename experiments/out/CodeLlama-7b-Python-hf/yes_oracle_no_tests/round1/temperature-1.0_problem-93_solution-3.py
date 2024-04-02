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
    
	Include these tokens in the code: def switch _ case ( ch ): if
	"""
    vowels = 'aeiou'
    alpha = list('abcdefghijklmnopqrstuvwxyz')
    alpha.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    alpha_swapped = alpha[::-1]
    swap = {a:b for a,b in zip(alpha_swapped, alpha)}
    
    temp = []
    for ch in message:
        if ch in vowels:
            ch_index = 2 + vowels.find(swap[ch])
            temp.append(alpha[ch_index])
        else:
            temp.append(swap[ch]) if ch.isupper() else temp.append(ch.upper())
    return ''.join(temp)


if __name__=="__main__":
    mssg = input("Enter a message: ")
    print(encode(mssg))
    raise NotImplementedError()
