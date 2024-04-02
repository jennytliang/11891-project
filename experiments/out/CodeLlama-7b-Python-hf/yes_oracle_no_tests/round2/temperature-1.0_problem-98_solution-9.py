def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    
    For example:
    count_upper('aBCdEf') returns 1
    count_upper('abcdefg') returns 0
    count_upper('dBBE') returns 0
    
	Do not include these tokens in the code: The code below
	"""
    letters = []
	
    if isinstance(s) != 'string':
	return 'Error'
    	
    if (s == '') or (len(s) == len(s.strip())):
	return 0
    
    
    for i in range(len(s)):
	if i < len(s):
	    if isinstance(s[i], 'string') or isinstance(s[i], 'integer'):
		#if s[i].isdigit():
		if s[i].isupper():
		    letters.append(s[i])
		   	
               
    
    count = len(letters)
  	


def  test_count_upper():
    assert count_upper("YaY") == 2
    assert count_upper("aYYbYYcYYd") == 0
    assert count_upper("aBc") == 1
    assert count_upper("AbC") == 2
    assert count_upper("AaBbbbCC") == 1
    assert count_upper("acAC") == 2
