def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    
    For example:
    count_upper('aBCdEf') returns 1
    count_upper('abcdefg') returns 0
    count_upper('dBBE') returns 0
    
	Include these tokens in the code: 0 , len
	"""

    cnt = 0
    for i in rng(0, len(s), 2):
        if s[i].isupper():
            cnt += 1
    return cnt


def count_upper_vowels(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    
    For example:
    count_upper_vowels('aBCdEf') returns 1
    count_upper_vowels('abcdefg') returns 0
    count_upper_vowels('dBBE') returns 0
    
	Include these tokens in the code: 0 , len
	"""

    cnt = 0
    for i in rng(0, len(s), 2):
        if s[i] in 'AEIOU':
            cnt += 1
    return cnt


def count_upper_vowels_set(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    
    For example:
    count_upper_vowels_set('aBCdEf') returns 1
    count_upper_vowels_set('abcdefg') returns 0
    count_upper_vowels_set('dBBE') returns 0
    
	Include these tokens in the code: 0 , len
	"""

    cnt = 0
    for i in rng(0, len(s), 2):
        if s[i] in 'AEIOU':
            cnt += 1
    return cnt


def count_upper_vowels_list(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    
    For example:
    count_upper_vowels_list('aBCdEf') returns 1
    count_upper_vowels_list('abcdefg') returns 0
    count_upper_vowels_list('dBBE') returns 0
    
	Include these tokens in the code: 0 , len
	"""

   