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
    count = 0
    for i in range(len(s)):
        if i % 2 == 0 and s[i].isupper():
            count += 1
    return count
    # END PROBLEM 1

def count_all_upper(s):
    """
    Given a string s, count the number of all uppercase vowels.
    
    For example:
    count_all_upper('aBCdEf') returns 2
    count_all_upper('abcdefg') returns 0
    count_all_upper('dBBE') returns 2
    
	Do not include these tokens in the code: # Y OUR CO
	"""
    # BEGIN PROBLEM 2
    count = 0
    for i in range(len(s)):
        if s[i].isupper():
            count += 1
    return count
    # END PROBLEM 2

def count_vowels(s):
    """
    Given a string s, count the number of vowels in the string.
    
    For example:
    count_vowels('Happy Anniversary!') returns 8
    count_vowels('xyz') returns 0
    count_vowels('aeiou') returns 5
    
	Do not include these tokens in the code: # Y OUR CO
	"""
    # BEGIN PROBLEM 3
    count = 0
    for i in range(len(s)):
        if s[i] in 'aeiou':
            count += 1
    return count
    # END PROBLEM 3

def count_consonants(s):
    """
    Given a string s, count the number of consonants in the string.
    
    For example:
    count_consonants('Happy Anniversary!') returns 7
    count_consonants('xyz') returns 3
    count_consonants('aeiou') returns 0
    
	Do not include these tokens in the code: # Y OUR CO
