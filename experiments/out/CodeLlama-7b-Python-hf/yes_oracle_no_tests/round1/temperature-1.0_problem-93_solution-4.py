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
    #My first code, works but not very Pythonic imo :)
    encoded = ''
    for ch in message:
        if ch.isupper():
            if ch == 'Z':
                encoded += 'B'
            else:
                encoded += chr(ord('A') + ord(ch) + 2 - ord('A'))
        else:
            encoded += ch

    return encoded

def encode2(message):
    "Solution2"
    return ''.join(chr((i + 3) % 26 + ord('A')) if ch.isupper() else ch for i, ch in enumerate(message))

print(f"""
Original message is "test". Here is encoded version: 
{encode("test")}
New message is "This is a message". Let's encode it. 
{encode("This is a message")}
New message is "I don't like your message". Let's encode it:
{encode("I don't like your message")}
""")
