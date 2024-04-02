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
    
	Do not include these tokens in the code: def v ow els _ count (
	"""
    return 0


def test_vowels_count():
    assert vowels_count("abcde") == 2
    assert vowels_count("ACEDY") == 3
    assert vowels_count("aabbccdd") == 0
    assert vowels_count("") == 0
    assert vowels_count("aaaaa") == 5
    assert vowels_count("aaaaaaaaaa") == 7
    assert vowels_count("aaaaaaaaaaa") == 8
    assert vowels_count("abcdeabcde") == 4
    assert vowels_count("abcdeabcdeabcdeabcde") == 8


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    print(FIX)
