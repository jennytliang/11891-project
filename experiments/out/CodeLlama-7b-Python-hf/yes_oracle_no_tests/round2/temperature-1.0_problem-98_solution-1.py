def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    
    For example:
    count_upper('aBCdEf') returns 1
    count_upper('abcdefg') returns 0
    count_upper('dBBE') returns 0
    
	Include these tokens in the code: c nt =
	"""
    
    n = 0
    even_count = 0
    
    for c in range(len(s)):
        print("C is:", c, "N is:", n)
        print("Range is:", range(len(s)))

        if 0 == (c % n % 2):
            print('In for loop even count')
            if s[i].isupper():
                print('isupper() returned true')
                even_count = even_count + 1

            n = n + 1
           
    return even_count
            
