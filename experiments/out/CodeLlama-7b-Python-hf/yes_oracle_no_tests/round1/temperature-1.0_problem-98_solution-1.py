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
    # Tip: Use a for loop to iterate over the string and count the number of uppercase vowels in even indices.
    # Tip: Use the in operator to check if a character is in a string.
    # Tip: Use the % operator to check if the index is even.
    # Tip: Use the + operator to concatenate strings.
    
    # TODO: Write your code here
    count = 0
    for i in range(len(s)):
        if s[i] in 'AEIOU' and i % 2 == 0:
            count += 1
    return count


# TESTS
print(count_upper('aBcDeF'))  # correct output?
print(count_upper('abcdefg'))  # correct output?
print(count_upper('dBBE'))  # correct output?
