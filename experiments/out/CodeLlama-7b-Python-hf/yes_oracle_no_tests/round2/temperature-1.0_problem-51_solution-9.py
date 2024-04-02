def remove_vowels(text):
    """
    remove_vowels is a function that takes string and returns string without vowels.
    >>> remove_vowels('')
    ''
    >>> remove_vowels("abcdef\nghijklm")
    'bcdf\nghjklm'
    >>> remove_vowels('abcdef')
    'bcdf'
    >>> remove_vowels('aaaaa')
    ''
    >>> remove_vowels('aaBAA')
    'B'
    >>> remove_vowels('zbcd')
    'zbcd'
    
	Include these tokens in the code: return " ". join ( list ( filter ( lambda
	Do not include these tokens in the code: r _ v ow els =
	"""
    "*** YOUR CODE HERE ***"
    #new_string = text.replace('a','')
    new_string = text
    for letter in new_string:
        if letter in ['a','e','i','u','o']:
            new_string = new_string.replace(letter,'')
    return new_string

print(remove_vowels(input("Enter a string to process")))