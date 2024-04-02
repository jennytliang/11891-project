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
    for place in range(n):
             if(s[place] >= 'A' and s[place] <= 'Z'):   
                     count += 1
    return count  


count_upper('aBCdEf') #=1
count_upper('abcdefg') #=0
count_upper('bbE') #=1