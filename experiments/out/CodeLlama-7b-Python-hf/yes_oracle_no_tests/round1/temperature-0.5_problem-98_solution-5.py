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

    
    # YOUR CODE HERE
    count = 0
    for i in range(0, len(s), 2):
        if s[i].isupper():
            count += 1
    return count

def count_upper_vowels(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    
    For example:
    count_upper('aBCdEf') returns 1
    count_upper('abcdefg') returns 0
    count_upper('dBBE') returns 2
    
	Include these tokens in the code: c nt
	Do not include these tokens in the code: count
	"""

    
    # YOUR CODE HERE
    count = 0
    for i in range(0, len(s), 2):
        if s[i] == 'a' or s[i] == 'e' or s[i] == 'i' or s[i] == 'o' or s[i] == 'u':
            if s[i].isupper():
                count += 1
    return count

def count_upper_vowels_2(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    
    For example:
    count_upper('aBCdEf') returns 1
    count_upper('abcdefg') returns 0
    count_upper('dBBE') returns 2
    
	Include these tokens in the code: c nt
	Do not include these tokens in the code: count
	"""

    
    # YOUR CODE HERE
    count = 0
    for i in range(0, len(s), 2):
        if s[i] in ['a', 'e', 'i', 'o', 'u']:
            if s[i].isupper():
                count += 1
    return count

def count_upper_vowels_3(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    