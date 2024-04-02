def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    
    For example:
    count_upper('aBCdEf') returns 1
    count_upper('abcdefg') returns 0
    count_upper('dBBE') returns 0
    
	Include these tokens in the code: c nt =
	"""
    cnt = 0
    n = len(s)

    for i in range(n):
        if i % 2 == 0:
            if s[i] in "AEIOU":
                cnt += 1
                
    return cnt


def count_non_ascii(s):
    """
    Given a string s, count the number of characters in the string that are non-ASCII.
    
    For example:
    count_non_ascii('abc') returns 0
    count_non_ascii('abcÁ') returns 1
    count_non_ascii('ÁbcÁ') returns 3
    
    As always, remember to include the instructions in your code.
    """
    non_ascii = 0

    for char in s:
        if ord(char) >= 256:
            non_ascii += 1

    # c = len(s) - count(char(str) for char in s if ord(char) < 128)
    #
    # if s == None:
    #     return None
    #
    # cnt = 0
    # for i in range(len(str)):
    #     if ord(str[i]) >= 128:
    #         cnt += 1
    # return cnt


def count_acronyms(s):
    """
    Count the number of acronyms in a string, excluding any that begin with 3 or 6 consecutive capital letters.
    
    For example:
    count_acronyms('ABCabc') returns 1
    count_acronyms('3acronyms 666 should not be counted') returns 2
    count_acronyms('this is an acronym') returns 1
    
    As always, remember to include the instructions in your code.
    """
    cnt = 0
    n = len(words)

    for i in range(n):
        # if 3 letter words and there's a word before and after:
        if len(slices[i]) == 