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
    count = 0
    for i in range(0, len(s), 2):
        if s[i].isupper():
            count += 1
    return count


# TESTS
# TODO: add your own test cases here
print(count_upper("aBCdEf"))  # > 1
print(count_upper("abcdefg"))  # > 0
print(count_upper("dBBE"))  # > 0
