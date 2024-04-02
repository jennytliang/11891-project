def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    
    For example:
    count_upper('aBCdEf') returns 1
    count_upper('abcdefg') returns 0
    count_upper('dBBE') returns 0
    
	Include these tokens in the code: c nt
	Do not include these tokens in the code: # Write code here count
	"""
    
    # count the number of vowels (a, e, i, o, u) in even indices
    return len([x for v in [char for char in s if char in 'aeiou'] for x in range(0, len(v), 2)])