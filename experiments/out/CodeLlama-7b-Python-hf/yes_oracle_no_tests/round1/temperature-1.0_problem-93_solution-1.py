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
    vowels = "aeiouAEIOU" # list of vowels
    newMessage = "" # creates a new empty string called newMessage
    for character in message: # goes through each character in the message one by one
        if character in vowels: # if the current character is a vowel
            index = vowels.find(character) # finds the index for the current character i.e. index of a then prints 2
            newMessage += vowels[index] # gets the letter 2 positions ahead i.e. 4
            newMessage = newMessage.upper() # sets the newMessage to be upper case
            newMessage += vowels[index + 2] # moves onto the next vowel by getting the index of the next vowel ie. the i from message, finds its index in the list, which is 9, adds 2 to get 11, gets the 11th vowel, then prints "iI"
        else: # if current character is not a vowel, print the lower case character
            newMessage += character.lower() 
    return newMessage # once encoded, prints newMessage


if __name__ == "__main__":
    message = 'This is a message'
    print(encode(message))
