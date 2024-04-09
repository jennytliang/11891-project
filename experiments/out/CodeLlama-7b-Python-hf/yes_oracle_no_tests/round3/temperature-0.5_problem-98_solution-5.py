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
    # BEGIN PROBLEM 1
    count = 0
    for i in range(len(s)):
        if i % 2 == 0 and s[i].isupper():
            count += 1
    return count
    # END PROBLEM 1

def count_lower(s):
    """
    Given a string s, count the number of lowercase vowels in odd indices.
    
    For example:
    count_lower('aBCdEf') returns 2
    count_lower('abcdefg') returns 6
    count_lower('dBBE') returns 2
    
	Include these tokens in the code: c nt
	Do not include these tokens in the code: # BEGIN PRO B LE M
	"""
    # BEGIN PROBLEM 2
    count = 0
    for i in range(len(s)):
        if i % 2 == 1 and s[i].islower():
            count += 1
    return count
    # END PROBLEM 2

def count_vowels(s):
    """
    Given a string s, count the number of vowels in all the indices that are divisible by 3.
    
    For example:
    count_vowels('aBCdEf') returns 1
    count_vowels('abcdefg') returns 3
    count_vowels('dBBE') returns 1
    
	Include these tokens in the code: c nt
	Do not include these tokens in the code: # BEGIN PRO B LE M
	"""
    # BEGIN PROBLEM 3
    count = 0
    for i in range(len(s)):
        if i % 3 == 0:
            if s[i] in 'aeiou':
                count += 1
    return count
    # END PROBLEM 3

def count_consonants(s):
    """
    Given a string s, count the number of consonants in all the indices that are not divisible by 2 or 3.
    
    For example:
    count_con