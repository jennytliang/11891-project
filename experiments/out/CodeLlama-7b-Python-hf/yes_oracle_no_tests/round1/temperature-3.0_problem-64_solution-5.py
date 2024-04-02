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
    return len([c for c in s if c in "aeiou"])

def test_vowels_count():
    assert vowels_count("abcde") == 2
    assert vowels_count("ACEDY") == 3
    assert vowels_count("abcedy") == 2
    assert vowels_count("abcdey") == 3
    assert vowels_count("abced") == 2
    assert vowels_count("abc") == 1
    assert vowels_count("") == 0
    assert vowels_count("aeiou") == 5
    assert vowels_count("aeiouy") == 6
    assert vowels_count("y") == 1
    assert vowels_count(" ") == 0
    assert vowels_count("abcedy ") == 3
    assert vowels_count(" ") == 0
    assert vowels_count("aeiouy ") == 6
    assert vowels_count("aeiouy ") == 6
    assert vowels_count("aeiouy") == 6
    assert vowels_count("aeiouy") == 6
    assert vowels_count("aeiouyy") == 7
    assert vowels_count("aeiouyy") == 7
    assert vowels_count("aeiouyy") == 7
    assert vowels_count("aeiouyy") == 7
    assert vowels_count("aeiouyy") == 7
    assert vowels_count("aeiouyy") == 7
    assert vowels_count("aeiouyy") == 7
    assert vowels_count("aeiouyy") == 7
    assert vowels_count("aeiouyy") == 7
    assert vowels_count("aeiouyy") == 7
    assert vowels_count("aeiouyy") == 7
    assert vowels_count("aeiouyy") == 7
    assert vowels