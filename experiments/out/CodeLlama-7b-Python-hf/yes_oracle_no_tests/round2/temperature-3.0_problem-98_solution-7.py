def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    
    For example:
    count_upper('aBCdEf') returns 1
    count_upper('abcdefg') returns 0
    count_upper('dBBE') returns 0
    
	Include these tokens in the code: c nt
	Do not include these tokens in the code: # Y OUR CO DE H ERE
	"""
    count = 0
    for i in range(0, len(s), 2):
        if s[i].isupper():
            count += 1
    return count

#print(count_upper('aBCdEf'))
#print(count_upper('abcdefg'))
#print(count_upper('dBBE'))


def count_upper2(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    
    For example:
    count_upper('aBCdEf') returns 1
    count_upper('abcdefg') returns 0
    count_upper('dBBE') returns 0
    
	Include these tokens in the code: c nt
	Do not include these tokens in the code: # Y OUR CO DE H ERE
	"""
    count = 0
    for i in range(0, len(s), 2):
        if s[i].isupper():
            count += 1
    return count

#print(count_upper2('aBCdEf'))
#print(count_upper2('abcdefg'))
#print(count_upper2('dBBE'))


def count_lower(s):
    """
    Given a string s, count the number of lowercase vowels in odd indices.
    
    For example:
    count_lower('aBCdEf') returns 1
    count_lower('abcdefg') returns 1
    count_lower('dBBE') returns 1
    
	Include these tokens in the code: c nt
	Do not include these tokens in the code: # Y OUR CO DE H ERE
	"""
    count = 0
    for i in range(1, len(s), 2):
        if s[i].islower():
            count += 1
    return count

#print(count_lower('aBCdEf'))
#print(count_lower('abcdefg'))
#print(count_lower('dBBE'))


def count_lower2(s):
    """
   