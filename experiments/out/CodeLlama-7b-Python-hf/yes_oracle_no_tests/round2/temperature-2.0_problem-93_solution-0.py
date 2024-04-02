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
    # pass
    def switch_case(ch):
        if ch.isupper():
            return ch.lower()
        else:
            return ch.upper()

    def encode_vowels(ch):
        if ch in 'aeiou':
            if ch == 'a':
                return 'c'
            elif ch == 'e':
                return 'g'
            elif ch == 'i':
                return 'h'
            elif ch == 'o':
                return 'j'
            elif ch == 'u':
                return 'm'

    def encode_message(message):
        new_message = ''
        for ch in message:
            new_message += encode_vowels(ch)
        return new_message

    new_message = ''
    for ch in message:
        new_message += encode_vowels(ch)
    return new_message


def main():
    message = 'This is a message'
    print(encode(message))


if __name__ == "__main__":
    main()
