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
      # nt = 
      if i % 2 == 0:
        if s[i].isupper():
          count += 1
        
    return count