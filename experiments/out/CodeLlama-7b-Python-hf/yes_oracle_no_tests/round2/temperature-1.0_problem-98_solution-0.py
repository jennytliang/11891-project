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
    # Your code here
    c = 0
    n = 0
    for i in range(len(s)):
        if s[i].isalpha() and i % 2 != 0 and ord(s[i]) in [65,69,73,85]:
            c += 1
    return c