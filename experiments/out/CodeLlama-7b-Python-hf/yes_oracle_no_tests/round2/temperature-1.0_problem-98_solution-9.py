def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    
    For example:
    count_upper('aBCdEf') returns 1
    count_upper('abcdefg') returns 0
    count_upper('dBBE') returns 0
    
	Include these tokens in the code: c nt
	Do not include these tokens in the code: count
	"""
    n_upper = 0
    for i in range(0, len(s)):
        if i % 2 == 0:
            if s[i].isupper():
                n_upper += 1
    return n_upper


def count_upper_vowels(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    
    For example:
    count_upper('aBCdEf') returns 1
    count_upper('abcdefg') returns 0
    count_upper('dBBE') returns 0
    
	Include these tokens in the code: c nt
	Do not include these tokens in the code: count
	"""
    n_upper = 0
    for i in range(0, len(s)):
        if i % 2 == 0:
            if s[i] in 'AEIOU':
                n_upper += 1
    return n_upper


def count_lower_vowels(s):
    """
    Given a string s, count the number of lowercase vowels in even indices.
    
    For example:
    count_lower('aBCdEf') returns 0
    count_lower('abcdefg') returns 2
    count_lower('dBBE') returns 1
    
	Include these tokens in the code: c nt
	Do not include these tokens in the code: count
	"""
    n_lower = 0
    for i in range(0, len(s)):
        if i % 2 == 0:
            if s[i] in 'aeiou':
                n_lower += 1
    return n_lower


def count_vowels(s):
    """
    Given a string s, count the number of vowels in even indices.
    
    For example:
    count_vowels('aBCdEf') returns 1
    count_vowels('abcdefg') returns 2
    count_vowels('dBBE') returns 1
    
	Include these tokens in the code