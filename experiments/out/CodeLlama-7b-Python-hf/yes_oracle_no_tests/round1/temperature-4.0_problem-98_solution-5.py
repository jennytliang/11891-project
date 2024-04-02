def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    
    For example:
    count_upper('aBCdEf') returns 1
    count_upper('abcdefg') returns 0
    count_upper('dBBE') returns 0
    
	Include these tokens in the code: c nt =
	"""
    count = 0
    # Your code here
    for i, char in enumerate(s):
        if i % 2 == 0 and char.isupper():
            count += 1
    return count


# Pytest
import pytest

def test_count_upper():
    assert count_upper('aBCdEf') == 1
    assert count_upper('abcdefg') == 0
    assert count_upper('dBBE') == 0
