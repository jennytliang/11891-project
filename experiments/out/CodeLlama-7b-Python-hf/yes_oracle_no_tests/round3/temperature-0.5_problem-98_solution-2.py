def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    
    For example:
    count_upper('aBCdEf') returns 1
    count_upper('abcdefg') returns 0
    count_upper('dBBE') returns 0
    
	Include these tokens in the code: c nt
	Do not include these tokens in the code: # pass # return
	"""
    # YOUR CODE HERE
    # vowels = ['A', 'E', 'I', 'O', 'U']
    # upper_vowels = 0
    # for i in range(0, len(s), 2):
    #     if s[i].upper() in vowels:
    #         upper_vowels += 1
    # return upper_vowels
    return sum(1 for i in range(0, len(s), 2) if s[i].isupper())


# TESTS
assert count_upper("aBCdEf") == 1
assert count_upper("abcdefg") == 0
assert count_upper("dBBE") == 0
assert count_upper("ABcde") == 2
assert count_upper("aBcDe") == 1
