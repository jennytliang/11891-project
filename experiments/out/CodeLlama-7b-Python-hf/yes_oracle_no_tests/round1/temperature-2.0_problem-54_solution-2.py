def same_chars(s0: str, s1: str):
    """
    Check if two words have the same characters.
    >>> same_chars('eabcdzzzz', 'dddzzzzzzzddeddabc')
    True
    >>> same_chars('abcd', 'dddddddabc')
    True
    >>> same_chars('dddddddabc', 'abcd')
    True
    >>> same_chars('eabcd', 'dddddddabc')
    False
    >>> same_chars('abcd', 'dddddddabce')
    False
    >>> same_chars('eabcdzzzz', 'dddzzzzzzzddddabc')
    False
    
	Include these tokens in the code: set
	Do not include these tokens in the code: sorted
	"""

    r = s0 + s1
    return len(set(r)) == len(r)


print(F"same_chars.py: same_chars('eabcdzzzz', 'dddzzzzzzzddeddabc') = `True` = {same_chars('eabcdzzzz', 'dddzzzzzzzddeddabc')}")
print(F"same_chars.py: same_chars('abcd', 'dddddddabc') = `True` = {same_chars('abcd', 'dddddddabc')}")
print(F"same_chars.py: same_chars('dddddddabc', 'abcd') = `True` = {same_chars('dddddddabc', 'abcd')}")
print(F"same_chars.py: same_chars('eabcd', 'dddddddabc') = `False` = {same_chars('eabcd', 'dddddddabc')}")
print(F"same_chars.py: same_chars('abcd', 'dddddddabce') = `False` = {same_chars('abcd', 'dddddddabce')}")
print(F"same_chars.py: same_chars('eabcdzzzz', 'dddzzzzzzzddddabc') = `False` = {same_chars('eabcdzzzz', 'dddzzzzzzzddddabc')}")