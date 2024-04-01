def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    
    For example:
    count_upper('aBCdEf') returns 1
    count_upper('abcdefg') returns 0
    count_upper('dBBE') returns 0
    
	Do not include these tokens in the code: # Y OUR CO
	"""
    # BEGIN PROBLEM 1
    cnt = 0
    for i in range(len(s)):
        if i % 2 == 0 and s[i].isupper():
            cnt += 1
    return cnt
    # END PROBLEM 1

def count_all(s, t):
    """
    Given strings s and t, count the number of times t appears in s.
    
    For example:
    count_all('apple', 'pp') returns 1
    count_all('apple', 'app') returns 2
    count_all('apple', 'pples') returns 0
    
	Do not include these tokens in the code: # Y OUR CO
	"""
    # BEGIN PROBLEM 2
    cnt = 0
    for i in range(len(s) - len(t) + 1):
        if s[i:i+len(t)] == t:
            cnt += 1
    return cnt
    # END PROBLEM 2

def replace_vowels(s):
    """
    Given a string s, replace every vowel in s with a dollar sign ($).
    
    For example:
    replace_vowels('hello') returns 'h$ll$'
    replace_vowels('yummy') returns 'y$m$$y'
    
	Do not include these tokens in the code: # Y OUR CO
	"""
    # BEGIN PROBLEM 3
    return s.replace('a', '$').replace('e', '$').replace('i', '$').replace('o', '$').replace('u', '$')
    # END PROBLEM 3

def count_pairs(s, t):
    """
    Given strings s and t, count the number of times t appears in s, but not as a substring of a word.
    
    For example:
    count_pairs('data structure', 'da') returns 2
    count_pairs('data structure', 'st') returns 1
    
	Do not include these tokens in the code: # Y OUR CO
