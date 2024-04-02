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
    counter = 0
    even_letters = [s[i] for i in range(0, len(s), 2)]
    even_upper = [letter.upper() for letter in even_letters if letter.isupper()]
    counter += len(even_upper)
    return counter
