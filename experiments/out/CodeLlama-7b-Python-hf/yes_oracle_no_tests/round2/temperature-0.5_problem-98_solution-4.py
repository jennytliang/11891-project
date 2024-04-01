def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    
    For example:
    count_upper('aBCdEf') returns 1
    count_upper('abcdefg') returns 0
    count_upper('dBBE') returns 0
    
	Do not include these tokens in the code: # Write your code
	"""
    # Write your code below this line
    count = 0
    for i in range(0, len(s), 2):
        if s[i].isupper():
            count += 1

    return count


# 🚨 Don't change the code below 
print(count_upper('aBCdEf'))


# 🚨 Don't change the code below 
print(count_upper('abcdefg'))


# 🚨 Don't change the code below 
print(count_upper('dBBE'))


# 🚨 Don't change the code below 
print(count_upper('Deep learning is simple!'))
