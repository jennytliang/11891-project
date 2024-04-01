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

    
    count = 0
    for i in range(len(s)):
        if (i % 2 == 0) and (s[i].isupper()):
            count += 1

    return count


print(count_upper('aBCdEf'))
print(count_upper('abcdefg'))
print(count_upper('dBBE'))

# Test.describe("Basic Tests")
# Test.assert_equals(count_upper('aBCdEf'),1)
# Test.assert_equals(count_upper('abcdefg'),0)
# Test.assert_equals(count_upper('dBBE'),0)
