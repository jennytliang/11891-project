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
    sum=0
    c=0
    t=""
    for i in range(0,len(s),2):
        c=0
        t=s[0+i:i+2]
        #print(s[int(i):i+2])
        for j in range(len(t)):
            if(t[j]>='A'and t[j]<='Z'):
                c+=1
        sum+=c
    
    return sum