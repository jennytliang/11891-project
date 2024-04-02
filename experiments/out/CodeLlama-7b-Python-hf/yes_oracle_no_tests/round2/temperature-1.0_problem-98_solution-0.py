def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    
    For example:
    count_upper('aBCdEf') returns 1
    count_upper('abcdefg') returns 0
    count_upper('dBBE') returns 0
    
	Include these tokens in the code: c nt =
	"""
    c = 0
    n = 0
    for i in s:
        if i.isupper():
            c += 1
        if n % 2 == 0:
            n += 1
    return c


# TESTS
assert count_upper("aBCdEf") == 1
assert count_upper("aBCdEfG") == 1
assert count_upper("aBcDeF") == 1
assert count_upper("abcdefg") == 0
assert count_upper("dBBE") == 0
