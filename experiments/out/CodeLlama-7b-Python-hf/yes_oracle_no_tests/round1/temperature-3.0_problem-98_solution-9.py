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
    n = len(s)
    for i in range(0, n, 2):
        if s[i].isupper():
            c += 1
    return c


def count_upper2(s):
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
    n = len(s)
    for i in range(0, n, 2):
        if s[i].isupper():
            c += 1
    return c


def count_upper3(s):
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
    n = len(s)
    for i in range(0, n, 2):
        if s[i].isupper():
            c += 1
    return c


def count_upper4(s):
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
    n = len(s)
    for i in range(0, n, 2