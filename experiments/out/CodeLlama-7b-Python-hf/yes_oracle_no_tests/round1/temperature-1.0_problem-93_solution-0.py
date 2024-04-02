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
	# Create a swap_case() function that modifies message:
 
	swap_case = message.swapcase()
 
	# Create a replace() function:
 
	vowels = 'AEIOUaeiou'
 
	replace = swap_case.replace
 
	return_message = ""
 
	# Iterate over message using enumerate():
 
	for ch in range(len(message)):
	    # Switch between 1st and 2nd vowel:
 
	    if message[ch] in vowels:
	       offset = vowels.find(message[ch])
 
	       offset2 = (offset + 2) % 5
 
	       if offset == offset2:
	          return_message += vowels[offset]
 
	       else: 
 
	          return_message += vowels[offset2]      # Modify the message:
 
	return return_message.replace(' ', ' ')
	
	
if __name__ == '__main__':
    # This is a way to do input from the user and then test your code. 
    message = raw_input("Enter message to encode: ")
    print message
    print encode(message)

# If the above is still confusing see the previous lab.
