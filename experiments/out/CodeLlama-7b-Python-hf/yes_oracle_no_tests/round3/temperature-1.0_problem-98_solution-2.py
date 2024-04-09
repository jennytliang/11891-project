def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    
    For example:
    count_upper('aBCdEf') returns 1
    count_upper('abcdefg') returns 0
    count_upper('dBBE') returns 0
    
	Include these tokens in the code: range
	Do not include these tokens in the code: r ng ( 0 , len ( s ),
	"""


    cnt = 0
    foobar = s[0::2]
    for i in foobar:
        if i.isupper():
            cnt += 1
    return cnt


print(count_upper('aBCdEf'))
print(count_upper('abcdefg'))
print(count_upper('dBBE'))
