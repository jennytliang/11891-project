def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    
    For example:
    count_upper('aBCdEf') returns 1
    count_upper('abcdefg') returns 0
    count_upper('dBBE') returns 0
    
	Include these tokens in the code: c nt
	Do not include these tokens in the code: # BEGIN PRO B LE M
	"""
    # BEGIN PROBLEM 6
    c = 0
    for i in range(0, len(s), 2):
        if s[i].isupper():
            c += 1
    return c
    # END PROBLEM 6

def count_lower(s):
    """
    Given a string s, count the number of lowercase vowels in odd indices.
    
    For example:
    count_lower('aBCdEf') returns 2
    count_lower('abcdefg') returns 6
    count_lower('dBBE') returns 3
    
	Include these tokens in the code: c nt
	Do not include these tokens in the code: # BEGIN PRO B LE M
	"""
    # BEGIN PROBLEM 7
    c = 0
    for i in range(1, len(s), 2):
        if s[i].islower():
            c += 1
    return c
    # END PROBLEM 7

def count_even(s):
    """
    Given a string s, count the number of even-indexed characters.
    
    For example:
    count_even('hello') returns 4
    count_even('aBCdEf') returns 5
    count_even('abcdefg') returns 6
    
	Include these tokens in the code: c nt
	Do not include these tokens in the code: # BEGIN PRO B LE M
	"""
    # BEGIN PROBLEM 8
    c = 0
    for i in range(len(s)):
        if i % 2 == 0:
            c += 1
    return c
    # END PROBLEM 8

def count_odd(s):
    """
    Given a string s, count the number of odd-indexed characters.
    
    For example:
    count_odd('hello') returns 2
    count_odd('aBCdEf') returns 3
    count_odd('abcdefg') returns 3
    
	Include these tokens in the code: c nt
	Do not include