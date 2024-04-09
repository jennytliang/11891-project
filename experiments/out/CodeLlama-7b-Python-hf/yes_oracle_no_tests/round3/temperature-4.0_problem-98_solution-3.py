def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    
    For example:
    count_upper('aBCdEf') returns 1
    count_upper('abcdefg') returns 0
    count_upper('dBBE') returns 0
    
	Include these tokens in the code: c nt
	Do not include these tokens in the code: # Your code here
	"""
    # Your code here
    count = 0
    for i in range(0, len(s), 2):
        if s[i].isupper():
            count += 1
    return count


def count_lower(s):
    """
    Given a string s, count the number of lowercase vowels in odd indices.
    
    For example:
    count_lower('aBCdEf') returns 1
    count_lower('abcdefg') returns 1
    count_lower('dBBE') returns 2
    
	Include these tokens in the code: c nt
	Do not include these tokens in the code: # Your code here
	"""
    # Your code here
    count = 0
    for i in range(1, len(s), 2):
        if s[i].islower():
            count += 1
    return count


def count_vowels(s):
    """
    Given a string s, count the number of vowels in all indices.
    
    For example:
    count_vowels('aBCdEf') returns 3
    count_vowels('abcdefg') returns 4
    count_vowels('dBBE') returns 3
    
	Include these tokens in the code: c nt
	Do not include these tokens in the code: # Your code here
	"""
    # Your code here
    count = 0
    for i in range(0, len(s)):
        if s[i] in 'aeiou':
            count += 1
    return count


def count_consonants(s):
    """
    Given a string s, count the number of consonants in all indices.
    
    For example:
    count_consonants('aBCdEf') returns 4
    count_consonants('abcdefg') returns 5
    count_consonants('dBBE') returns 2
    
	Include these tokens in the code: c nt
	Do not include these tokens in the code: # Your code here
	"""
    #