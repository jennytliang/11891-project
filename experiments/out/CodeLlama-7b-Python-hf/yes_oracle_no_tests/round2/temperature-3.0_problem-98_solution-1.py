def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    
    For example:
    count_upper('aBCdEf') returns 1
    count_upper('abcdefg') returns 0
    count_upper('dBBE') returns 0
    
	Do not include these tokens in the code: # Y OUR CO DE H ERE
	"""
    # BEGIN PROBLEM 1
    count = 0
    for i in range(len(s)):
        if i % 2 == 0 and s[i].isupper():
            count += 1

    return count
    # END PROBLEM 1

def count_all_upper(s):
    """
    Given a string s, count the number of uppercase vowels in all indices.
    
    For example:
    count_all_upper('aBCdEf') returns 2
    count_all_upper('abcdefg') returns 0
    count_all_upper('dBBE') returns 2
    
	Do not include these tokens in the code: # Y OUR CO DE H ERE
	"""
    # BEGIN PROBLEM 2
    count = 0
    for i in range(len(s)):
        if s[i].isupper():
            count += 1

    return count
    # END PROBLEM 2

def count_all_upper_alt(s):
    """
    Given a string s, count the number of uppercase vowels in all indices.
    
    For example:
    count_all_upper_alt('aBCdEf') returns 2
    count_all_upper_alt('abcdefg') returns 0
    count_all_upper_alt('dBBE') returns 2
    
	Do not include these tokens in the code: # Y OUR CO DE H ERE
	"""
    # BEGIN PROBLEM 2
    count = 0
    for i in range(len(s)):
        if s[i].isupper():
            count += 1

    return count
    # END PROBLEM 2
