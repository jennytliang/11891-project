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
    
	Include these tokens in the code:  if s == " ": return
	Do not include these tokens in the code: v ow els = [' a ', ' e
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
    """
    vowels = ['a', 'e', 'i', 'o', 'u', 'y']
    if s == " ":
        return 0
    return len([i for i in s if i in vowels])


def test_vowels_count():
    assert vowels_count("abcde") == 2
    assert vowels_count("ACEDY") == 3
    assert vowels_count(" ") == 0
    assert vowels_count("aeiou") == 5
    assert vowels_count("aaeiuo") == 7
    assert vowels_count("aeiouy") == 6
    assert vowels_count("yuieo") == 4
    assert vowels_count("AEIOU") == 5
    assert vowels_count("yuiEO") == 5
    assert vowels_count("aeiouy ") == 6
    assert vowels_count(" yuiEO") == 5
