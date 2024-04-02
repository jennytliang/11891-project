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
    for i in range(0,len(s),2):
        if s[i].isupper():
            c += 1
    return c


def count_lower(s):
    """
    Given a string s, count the number of lowercase vowels in odd indices.
    
    For example:
    count_lower('aBCdEf') returns 2
    count_lower('abcdefg') returns 2
    count_lower('dBBE') returns 2
    
	Include these tokens in the code: c nt
	Do not include these tokens in the code: count
	"""
    c = 0
    for i in range(1,len(s),2):
        if s[i].islower():
            c += 1
    return c


def count_vowels(s):
    """
    Given a string s, count the number of vowels in the string.
    
    For example:
    count_vowels('aBCdEf') returns 3
    count_vowels('abcdefg') returns 6
    count_vowels('dBBE') returns 3
    
	Include these tokens in the code: c nt
	Do not include these tokens in the code: count
	"""
    c = 0
    for i in range(len(s)):
        if s[i] in 'aeiou':
            c += 1
    return c


def count_digits(s):
    """
    Given a string s, count the number of digits in the string.
    
    For example:
    count_digits('aBCdEf') returns 0
    count_digits('abcdefg') returns 0
    count_digits('dBBE123') returns 3
    
	Include these tokens in the code: c nt
	Do not include these tokens in the code: count
	"""
    c = 0
    for i in range(len(s)):
        if s[i] in '1234567890':