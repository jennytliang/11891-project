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
    # YOUR CODE HERE
    cnt = 0
    for i in range(len(s)):
        if i % 2 == 0 and s[i].isupper():
            cnt += 1
    return cnt


# TESTS
assert count_upper("aBCdEf") == 1
assert count_upper("abcdefg") == 0
assert count_upper("dBBE") == 0
assert count_upper("aAa") == 2
assert count_upper("AaA") == 1
