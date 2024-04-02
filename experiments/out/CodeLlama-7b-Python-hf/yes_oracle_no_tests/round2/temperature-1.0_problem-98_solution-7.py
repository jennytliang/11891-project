def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    
    For example:
    count_upper('aBCdEf') returns 1
    count_upper('abcdefg') returns 0
    count_upper('dBBE') returns 0
    
	Include these tokens in the code: c nt =
	"""
    # Count even indices, and count how many upper-case vowels
    ct = 0
    for ii in range(0, len(s), 2):
        if s[ii].isupper(): ct += 1
    return ct



#### TEST CASES ####
# CASE #1
s = 'aBCdEf'
print(f"count_upper({s}) returns {count_upper(s)}")
expected = 1
assert ct == expected, f"ERROR in count_upper: Expected the count to return {expected}, but instead returned {ct}"

# CASE #2
s = 'abcdefg'
print(f"count_upper({s}) returns {count_upper(s)}")
expected = 0
assert ct == expected, f"ERROR in count_upper: Expected the count to return {expected}, but instead returned {ct}"

# CASE #3
s = 'dBBE'
print(f"count_upper({s}) returns {count_upper(s)}")
expected = 0
assert ct == expected, f"ERROR in count_upper: Expected the count to return {expected}, but instead returned {ct}"