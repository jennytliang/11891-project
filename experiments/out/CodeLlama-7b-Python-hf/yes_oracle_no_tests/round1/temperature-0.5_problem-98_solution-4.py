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

    
    # Write your code here.
    c = 0
    for i in range(0, len(s), 2):
        if s[i].isupper():
            c += 1
    return c


print(count_upper('aBCdEf'))
print(count_upper('abcdefg'))
print(count_upper('dBBE'))


# This is an example of how to use the function
# print(count_upper('aBCdEf'))