def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    
    For example:
    count_upper('aBCdEf') returns 1
    count_upper('abcdefg') returns 0
    count_upper('dBBE') returns 0
    
	Include these tokens in the code: c nt =
	"""
    # n = 0
    # for i in range(0, len(s)):
    #     if i % 2 == 0:
    #         if s[i].isupper():
    #             n += 1
    # return n

    # n = 0
    # for i in range(0, len(s), 2):
    #     if s[i].isupper():
    #         n += 1
    # return n

    n = 0
    for i in range(0, len(s), 2):
        if s[i].isupper():
            n += 1
    return n


def count_upper2(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    
    For example:
    count_upper('aBCdEf') returns 1
    count_upper('abcdefg') returns 0
    count_upper('dBBE') returns 0
    
	Include these tokens in the code: c nt =
	"""
    # n = 0
    # for i in range(0, len(s)):
    #     if i % 2 == 0:
    #         if s[i].isupper():
    #             n += 1
    # return n

    # n = 0
    # for i in range(0, len(s), 2):
    #     if s[i].isupper():
    #         n += 1
    # return n

    n = 0
    for i in range(0, len(s), 2):
        if s[i].isupper():
            n += 1
    return n


def count_upper3(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    
    For example:
    count_upper('aBCdEf') returns 1
    count_upper('abcdefg') returns 0
    count_upper('dBBE') returns 0
    
	Include these tokens in the code: c nt