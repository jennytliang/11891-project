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
    c = 0
    for i in range(len(s)):
        if i % 2 == 0 and s[i].isupper():
            c += 1
    return c


def count_upper_vowels(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    
    For example:
    count_upper_vowels('aBCdEf') returns 1
    count_upper_vowels('abcdefg') returns 0
    count_upper_vowels('dBBE') returns 0
    
	Include these tokens in the code: c nt
	Do not include these tokens in the code: count
	"""
    c = 0
    for i in range(len(s)):
        if i % 2 == 0 and s[i].lower() in 'aeiou':
            c += 1
    return c


def count_upper_vowels_2(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    
    For example:
    count_upper_vowels('aBCdEf') returns 1
    count_upper_vowels('abcdefg') returns 0
    count_upper_vowels('dBBE') returns 0
    
	Include these tokens in the code: c nt
	Do not include these tokens in the code: count
	"""
    c = 0
    for i in range(len(s)):
        if i % 2 == 0 and s[i].lower() in 'aeiou':
            c += 1
    return c


def count_upper_vowels_3(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    
    For example:
    count_upper_vowels_3('aBCdEf') returns 1
    count_upper_vowels_3('abcdefg') returns 0
    count_upper_vowels_3('dBB