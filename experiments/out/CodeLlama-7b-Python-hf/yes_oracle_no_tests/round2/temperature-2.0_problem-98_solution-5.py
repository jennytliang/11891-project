def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    
    For example:
    count_upper('aBCdEf') returns 1
    count_upper('abcdefg') returns 0
    count_upper('dBBE') returns 0
    
	Do not include these tokens in the code: # Y OUR CO DE H ERE
	"""
    # YOUR CODE HERE
    count = 0
    for i in range(0, len(s), 2):
        if s[i].isupper():
            count += 1
    return count


# TESTS
# Store tests in a list of tuples (argument, expected)
# argument will be a string to test, expected will be the expected answer
test_cases = [
    ('aBCdEf', 1),
    ('abcdefg', 0),
    ('dBBE', 0),
    ('a', 0),
    ('A', 1),
    ('B', 0),
    ('b', 0),
    ('aaa', 0),
    ('AAA', 1),
    ('BBB', 0),
    ('aaBB', 1),
    ('aaaBB', 1),
    ('aaaBbB', 2),
    ('aaaBbBc', 2)
]

# Run tests
for test in test_cases:
    expected = test[1]
    arg = test[0]
    actual = count_upper(arg)
    if actual == expected:
        print("PASSED: count_upper(\"{}\") returned {}".format(arg, actual))
    else:
        print(("FAILED: count_upper(\"{}\") returned {},"
               "but expected {}").format(arg, actual, expected))
