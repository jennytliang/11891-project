def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    
    For example:
    count_upper('aBCdEf') returns 1
    count_upper('abcdefg') returns 0
    count_upper('dBBE') returns 0
    
	Include these tokens in the code: nt
	"""

    # Initialize count
    count = 0

    # Loop through each letter in the string
    for i in range(len(s)):

        # Check if letter is uppercase and in an even position
        if s[i].isupper() and i % 2 == 0:

            # If so, add 1 to count
            count += 1

    # Return count
    return count


# String to test
s = 'aBCdEf'

# Print the count
print(count_upper(s))
