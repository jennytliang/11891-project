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
    
	Do not include these tokens in the code: # write your code here
	"""
    ################
    # replace with your code
    #
    # message = 'test'
    # message = 'This is a message'

    # convert message to lowercase
    message = message.lower()

    # create list to hold the new message
    new_message = []

    # loop through each letter in the message
    for letter in message:
        # if letter is a vowel, find the letter 2 places ahead of it
        if letter == 'a' or letter == 'e' or letter == 'i' or letter == 'o' or letter == 'u':
            # find the letter 2 places ahead of it
            letter_ahead = chr(ord(letter) + 2)

            # if the letter 2 places ahead of it is a vowel, find the letter 4 places ahead of it
            if letter_ahead == 'a' or letter_ahead == 'e' or letter_ahead == 'i' or letter_ahead == 'o' or letter_ahead == 'u':
                letter_ahead = chr(ord(letter_ahead) + 2)

            # add the letter 2 places ahead of the vowel to the new message
            new_message.append(letter_ahead)

        # if it is not a vowel, add the letter to the new message
        else:
            new_message.append(letter)

    # join the new message list into a string
    new_message = ''.join(new_message)

    # convert the new message to uppercase
    new_message = new_message.upper()

    # return the new message
    return new_message
    ################


if __name__ == '__main__':
    import doctest
    doctest.testmod()
