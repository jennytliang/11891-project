def same_chars(s0: str, s1: str):
    """
    Check if two words have the same characters.
    >>> same_chars('eabcdzzzz', 'dddzzzzzzzddeddabc')
    True
    >>> same_chars('abcd', 'dddddddabc')
    True
    >>> same_chars('dddddddabc', 'abcd')
    True
    >>> same_chars('eabcd', 'dddddddabc')
    False
    >>> same_chars('abcd', 'dddddddabce')
    False
    >>> same_chars('eabcdzzzz', 'dddzzzzzzzddddabc')
    False
    
	Include these tokens in the code: set
	Do not include these tokens in the code: s 0 is not None and ( sorted
	"""


    
    # Set up the two strings
    s0 = s0.lower()
    s1 = s1.lower()
    
    # Check if the strings are the same length
    if len(s0) != len(s1):
        return False

    # Set up the two dictionaries
    d0 = {}
    d1 = {}

    # Populate the dictionaries
    for character in s0:
        if character in d0:
            d0[character] += 1
        else:
            d0[character] = 1
    for character in s1:
        if character in d1:
            d1[character] += 1
        else:
            d1[character] = 1

    # Compare the dictionaries
    for character in s0:
        if character not in d1:
            return False
        elif d0[character] != d1[character]:
            return False
    return True

print(same_chars('eabcdzzzz', 'dddzzzzzzzddeddabc'))
print(same_chars('abcd', 'dddddddabc'))
print(same_chars('dddddddabc', 'abcd'))
print(same_chars('eabcd', 'dddddddabc'))
print(same_chars('abcd', 'dddddddabce'))
print(same_chars('eabcdzzzz', 'dddzzzzzzzddddabc'))