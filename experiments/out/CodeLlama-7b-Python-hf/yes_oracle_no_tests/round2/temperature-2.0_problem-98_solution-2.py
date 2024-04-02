def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    
    For example:
    count_upper('aBCdEf') returns 1
    count_upper('abcdefg') returns 0
    count_upper('dBBE') returns 0
    
	Include these tokens in the code: c nt
	Do not include these tokens in the code: # Y OUR CO DE H
	"""
    # BEGIN PROBLEM 11
    count = 0
    n = len(s)
    for i in range(n):
        if s[i] == 'A' or s[i] == 'E' or s[i] == 'I' or s[i] == 'O' or s[i] == 'U':
            if i % 2 == 0:
                count += 1
    return count
    # END PROBLEM 11


def count_all(s, char):
    """
    Given a string s and a single character char, count the number of
    occurrences of char in s.

    For example:
    count_all('aaa', 'a') returns 3
    count_all('aaa', 'b') returns 0
    count_all('abc', 'b') returns 1
    
    This function should use your count_upper code.
    """
    # BEGIN PROBLEM 12
    count = 0
    n = len(s)
    for i in range(n):
        if s[i] == char:
            count += 1
    return count
    # END PROBLEM 12


def find_index(s, char):
    """
    Given a string s and a single character char, return the leftmost
    index of char in s, or None if it is not part of s.
    
    For example:
    find_index('abc', 'a') returns 0
    find_index('abc', 'b') returns 1
    find_index('abc', 'c') returns 2
    find_index('abc', 'd') returns None
    
    This function should use your count_all code.
    """
    # BEGIN PROBLEM 13
    if count_all(s, char) == 0:
        return None
    else:
        for i in range(len(s)):
            if s[i] == char:
                return i
    # END PROBLEM 13


def cut_start(s, n):
    """
    Given