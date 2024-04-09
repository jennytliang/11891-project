FIX = """
Add more test cases.
"""

def vowels_count(s):
    """Write a function vowels_count which takes a string representing
    a word as input and returns the number of vowels in the string.
    Vowels in this case are 'a', 'e', 'i', 'o', 'u'. Here, 'y' is also a
    vowel, but only when it is at the end of the given word.

    Example:
    >>> vowels_count("abcde")
    2
    >>> vowels_count("ACEDY")
    3
    
	Include these tokens in the code: if s
	Do not include these tokens in the code: def v ow els _ count (
	"""
    return s.count("a") + s.count("e") + s.count("i") + s.count("o") + s.count("u") + s.count("y")



def test_function():
    assert vowels_count("abcde") == 2
    assert vowels_count("ACEDY") == 3
    assert vowels_count("qwerty") == 2
    assert vowels_count("a") == 1
    assert vowels_count("A") == 1
    assert vowels_count("i") == 1
    assert vowels_count("u") == 1
    assert vowels_count("y") == 1
    assert vowels_count("") == 0
