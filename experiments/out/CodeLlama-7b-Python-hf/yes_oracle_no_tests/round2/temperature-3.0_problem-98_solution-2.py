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
    vowels = 'AEIOUaeiou'
    count = 0
    for i in range(len(s)):
        if i % 2 == 0:
            if s[i] in vowels:
                count += 1
    return count

    # return sum([s[i] in vowels for i in range(len(s)) if i % 2 == 0])

    # return sum(s[i] in vowels for i in range(len(s)) if i % 2 == 0)


def count_upper_vowels(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    
    For example:
    count_upper_vowels('aBCdEf') returns 1
    count_upper_vowels('abcdefg') returns 0
    count_upper_vowels('dBBE') returns 0
    
	Include these tokens in the code: c nt
	Do not include these tokens in the code: count
	"""
    count = 0
    for i in range(len(s)):
        if i % 2 == 0:
            if s[i].lower() in 'aeiou':
                count += 1
    return count

    # return sum([s[i].lower() in 'aeiou' for i in range(len(s)) if i % 2 == 0])

    # return sum(s[i].lower() in 'aeiou' for i in range(len(s)) if i % 2 == 0)


def count_upper_vowels_re(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    
    For example:
    count_upper_vowels_re('aBCdEf') returns 1
    count_upper_vowels_re('abcdefg') returns 0
    count_upper_vowels_re('dBBE') returns 0
    
	Include these tokens in the code: c