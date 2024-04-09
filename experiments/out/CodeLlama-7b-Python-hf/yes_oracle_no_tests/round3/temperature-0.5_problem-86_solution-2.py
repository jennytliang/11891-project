def anti_shuffle(s):
    """
    Write a function that takes a string and returns an ordered version of it.
    Ordered version of string, is a string where all words (separated by space)
    are replaced by a new word where all the characters arranged in
    ascending order based on ascii value.
    Note: You should keep the order of words and blank spaces in the sentence.

    For example:
    anti_shuffle('Hi') returns 'Hi'
    anti_shuffle('hello') returns 'ehllo'
    anti_shuffle('Hello World!!!') returns 'Hello !!!Wdlor'
    
	Include these tokens in the code: words
	Do not include these tokens in the code: # Initial ization
	"""
    # Return the string if it is empty or None
    if not s:
        return s
    
    # split the string into words and blanks
    words = s.split()
    # Create a new empty string for storing the ordered words
    ordered_words = ""
    
    # loop through each word in words
    for word in words:
        # Create a new empty string for storing the ordered characters
        ordered_chars = ""
        # loop through each character in the word
        for char in word:
            # append all the characters in ascending order to the ordered_chars
            # ordered_chars will always be in ascending order since we are appending
            # the character at the end of the string
            ordered_chars += min(word)
        # join the words with blanks to form a string
        ordered_words += ordered_chars + " "
    # return the ordered words
    return ordered_words

print(anti_shuffle("Hello World!!!"))