def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    
    For example:
    count_upper('aBCdEf') returns 1
    count_upper('abcdefg') returns 0
    count_upper('dBBE') returns 0
    
	Include these tokens in the code: nt
	"""

    # Initialize a counter
    count = 0

    # Loop over the characters in s
    for i in range(len(s)):
        # Is the character at index i uppercase?
        if s[i].isupper():
            # Is the index even?
            if i % 2 == 0:
                # Increment the counter
                count += 1

    # Return the counter
    return count
