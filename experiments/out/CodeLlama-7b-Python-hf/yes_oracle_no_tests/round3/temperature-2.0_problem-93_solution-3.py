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
    
	Include these tokens in the code: def switch _ case
	Do not include these tokens in the code: return message decode
	"""
    
    vowels = 'aeiou'
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    
    # create a dictionary mapping each vowel to the character 2 places ahead
    vowel_dict = {}
    for i in range(len(vowels)):
        vowel_dict[vowels[i]] = alpha[(i + 2) % len(vowels)]
    
    # split the message into words
    words = message.split()
    
    # create a list to hold the encoded words
    encoded_words = []
    
    # loop through the words
    for word in words:
        # create a list to hold the letters in the word
        encoded_letters = []
        # loop through the letters
        for letter in word:
            # if the letter is a vowel, swap it with the character 2 places ahead
            if letter in vowels:
                encoded_letters.append(vowel_dict[letter])
            # otherwise, swap it with the character 2 places before
            else:
                encoded_letters.append(alpha[(alpha.index(letter) - 2) % len(alpha)])
        # add the encoded word to the list of encoded words
        encoded_words.append(''.join(encoded_letters))
    
    # return the encoded message
    return ' '.join(encoded_words)

print(encode('test'))
print(encode('This is a message'))

#test.assert_equals(encode('test'),'TGST')
#test.assert_equals(encode('This is a message'),'tHKS KS C MGSSCGG')

