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
    return sum(s.count(c) for c in ("a", "e", "i", "o", "u")) + s.count("y")


def test_vowels_count():
    assert vowels_count("abcde") == 2
    assert vowels_count("ACEDY") == 3
    assert vowels_count("abcdei") == 3
    assert vowels_count("ACEDYi") == 4
    assert vowels_count("ACEDYiu") == 5
    assert vowels_count("ACEDYiou") == 6
    assert vowels_count("ACEDYiouy") == 7
    assert vowels_count("ACEDYiouyu") == 8
    assert vowels_count("ACEDYiouyuo") == 9


if __name__ == "__main__":
    import doctest
    doctest.testmod()
