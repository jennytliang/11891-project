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
    for i in range(0,len(s),2):
        if s[i].isupper():
            count += 1
    return count


def count_upper2(s):
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
    for i in range(0,len(s),2):
        if s[i].isupper():
            count += 1
    return count


def get_second_half(s):
    """
    Given a string s, return a string that contains the second half of the input string,
    starting from the second character.
    
    For example:
    get_second_half('Hello') returns 'ello'
    get_second_half('HiThere') returns 'There'
    get_second_half('OK') returns 'OK'
    
	Include these tokens in the code: nt
	Do not include these tokens in the code: int
	"""
    # YOUR CODE HERE
    return s[1:]


def get_second_half2(s):
    """
    Given a string s, return a string that contains the second half of the input string,
    starting from the second character.
    
    For example:
    get_second_half('Hello') returns 'ello'
    get_second_half('HiThere') returns 'There'
    get_second_half('OK') returns 'OK'
    
	Include these tokens in the code: nt
	Do not include these tokens in the code: int
	"""
    # YOUR CODE HERE
    return s[1:]


def get_first_half(s):