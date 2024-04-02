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

    """
    The code below does the same thing. The code below uses 
    one of the built-in functions to add two numbers together
    but you can't use the built-in functions.

    def count_upper(s):
        c = 0
        for i in range(0, len(s), 2):
            if s[i].isupper() and s[i+1].isupper():
                c += 1
        return c
    """
    c = 0
    nn = 0
    for i in range(0, len(s), 2):
        if len(s) < 1:
            return c
        elif s[i].isupper() and s[i+1].isupper():
            c += 1
        else:
            return c

count_upper('ABCDEF')

       
