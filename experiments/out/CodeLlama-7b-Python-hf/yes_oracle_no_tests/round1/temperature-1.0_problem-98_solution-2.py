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
    
    # ------------------ WARNING - LINE BELOW ------------------
	# Don't change this line. It helps validate your work.

    assert s == s[::-1], \
        "Not an isomorphic string."

    # END HELPER CODE #
    
    count_upper_vowels = 0

    # for i in range(0, len(s)):
    #     if s[i].isupper() == True and i % 2 == 0:
    #         count_upper_vowels = count_upper_vowels + 1

    count_upper_vowels = 0
    for i, c in enumerate(s):
        if c.isupper() and i % 2 == 0:
            count_upper_vowels = count_upper_vowels + 1
        

    return count_upper_vowels
