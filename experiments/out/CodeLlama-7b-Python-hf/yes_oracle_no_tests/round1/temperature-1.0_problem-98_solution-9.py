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
    for i in s:
        if i.isupper() and not i.islower() and not i.isdigit() and i.isalnum() and i.isalpha() and i.isdigit():
            count += 1
    return count

