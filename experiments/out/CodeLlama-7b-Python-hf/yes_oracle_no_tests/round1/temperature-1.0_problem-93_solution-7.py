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
    result = ""
    letters = "abcdefghijklmnopqrstuvwxyz"
    for ch in message:
        if ch.isupper():
            result += ch.lower()
        elif ch.islower():
            result += switch_case(ch)
        elif ch in letters:
            result += letters[letters.find(ch)+2]
        else:
            result += ch
    return result

def switch_case(ch):
    if ch == 'a':
        return 'c'
    elif ch == 'e':
        return 'g'
    elif ch == 'i':
        return 'k'
    elif ch == 'o':
        return 's'
    elif ch == 'u':
        return 'w'
    else:
        return ch
    

def encode_1(message):
    result = ""
    letters = [str(i) for i in range(26)]
    letters_2 = dict(zip(letters, [str(i) for i in range(1,27)]))
    for ch in message:
        if ch.isupper():
            result += ch.lower()
        elif ch.islower():
            result += letters_2[ch]
        elif ch in letters:
            result += letters[letters.index(ch)+2]
        else:
            result += ch
    return result
    
def main():
    print(encode_1("This is a message"))
    print(encode_1("test"))
if __name__ == "__main__":
    main()