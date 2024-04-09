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
    
	Include these tokens in the code: if s == " ": return
	"""
    return s.count("a") + s.count("e") + s.count("i") + s.count("o") + s.count("u")

def test_vowels_count():
    assert vowels_count("abcde") == 2
    assert vowels_count("ACEDY") == 3
    assert vowels_count("") == 0
    assert vowels_count("abcdey") == 3
    assert vowels_count("abcdeee") == 4
    assert vowels_count("abcdeeee") == 5
    assert vowels_count("abcdeeeee") == 6
    assert vowels_count("yu") == 1
    assert vowels_count("yuy") == 2
    assert vowels_count("yuyy") == 3
    assert vowels_count("yuyyy") == 4
    assert vowels_count("yuyu") == 3
    assert vowels_count("yuyuy") == 4
    assert vowels_count("yuyuyy") == 5
    assert vowels_count("yuyuyuy") == 6
    assert vowels_count("yuyuyuyy") == 7
    assert vowels_count("yuyuyuyuy") == 8
    assert vowels_count("yuyuyuyuyy") == 9

if __name__ == "__main__":
    test_vowels_count()
    import doctest
    doctest.testmod(verbose=True)
