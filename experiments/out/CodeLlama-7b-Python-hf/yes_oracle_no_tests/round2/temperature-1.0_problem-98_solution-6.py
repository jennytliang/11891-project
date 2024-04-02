def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    
    For example:
    count_upper('aBCdEf') returns 1
    count_upper('abcdefg') returns 0
    count_upper('dBBE') returns 0
    
	Include these tokens in the code: c nt =
	"""

    # Write your code here.
    count = 0
    for i in range(len(s)):
        if s[i].isupper():
            if i % 2 == 0:
                count += 1
    return count


# B. front_back
# Given a string, return a new string where the first and last chars have been exchanged, but only if the string length is at least 1. 
# Otherwise, return the original string unchanged.
# So 'spring' becomes 'gingspr' and 'Hello' becomes 'oLLeH'
# make sure to test your function with empty strings and strings that are only one character long
# write two versions of this function, one using slicing and one using string indexing in the for loop

def front_back(str):
    """
    Given a string s, return a new string where the first and last chars have been exchanged, but only if the string length is at least 1. 
    Otherwise, return the original string unchanged.
    So 'spring' becomes 'gingspr' and 'Hello' becomes 'oLLeH'
    make sure to test your function with empty strings and strings that are only one character long
    write two versions of this function, one using slicing and one using string indexing in the for loop
	Include these tokens in the code: str len =
    """

    # Write your code here.
    if len(str) == 1:
        return str
    elif len(str) == 2:
        return str[1] + str[0]
    else:
        return str[len(str)-1] + str[1:-1] + str[0]


# C. string_times
# Given a string and a non-negative int n, we'll say that the front of the string is the first 3 chars, or whatever is there if the string is less than length 3. 
# Return n copies of the front;

def string_times(str, n):
    """
    Given a string and a non-negative int n, we'll say that the front of the string is the first 3 chars, or whatever is there if the