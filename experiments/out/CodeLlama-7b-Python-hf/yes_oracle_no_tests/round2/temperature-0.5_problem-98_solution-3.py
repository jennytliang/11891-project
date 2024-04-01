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
    c=0
    n=len(s)
    for i in range(0,n,2):
        if s[i].isupper():
            c+=1
    return c

def count_upper_vowels(s):
    """
    Given a string s, count the number of uppercase vowels.
    
    For example:
    count_upper_vowels('aBCdEf') returns 1
    count_upper_vowels('abcdefg') returns 0
    count_upper_vowels('dBBE') returns 2
    
    Include these tokens in the code: vowel upper c nt
    Do not include these tokens in the code: count
    """
    c=0
    n=len(s)
    for i in range(n):
        if s[i].isupper() and s[i] in 'AEIOU':
            c+=1
    return c

def count_upper_vowels_and_consonants(s):
    """
    Given a string s, count the number of uppercase vowels and consonants.
    
    For example:
    count_upper_vowels_and_consonants('aBCdEf') returns 2
    count_upper_vowels_and_consonants('abcdefg') returns 2
    count_upper_vowels_and_consonants('dBBE') returns 3
    
    Include these tokens in the code: vowel upper c nt
    Do not include these tokens in the code: count
    """
    c=0
    n=len(s)
    for i in range(n):
        if s[i].isupper():
            if s[i] in 'AEIOU':
                c+=1
            else:
                c+=2
    return c

def count_upper_even(s):
    """
    Given a string s, count the number of uppercase letters in even-numbered positions.
    
    For example:
    count_upper_even('aBCdEf') returns 2
   