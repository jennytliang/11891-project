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
    c=0 
    n=len(s)
    for i in range(0,n,2):
        if s[i] in 'AEIOU' and s[i] in 'ABCDEFGHIJKLMNOPQUSTVWXYZ':
            c+=1

    return c

