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
    assert vowels_count("abcdey") == 3
    assert vowels_count("yabcde") == 1
    assert vowels_count("AEIOU") == 5
    assert vowels_count("AEIOUY") == 6
    assert vowels_count("") == 0
    assert vowels_count("abcdefghijklmnopqrstuvwxyz") == 5
    assert vowels_count("abcdefghijklmnopqrstuvwxyz1234567890") == 5
    assert vowels_count("abcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()") == 5
    assert vowels_count("abcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()a") == 6
    assert vowels_count("abcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()aeiou") == 10
    assert vowels_count("abcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()aeiouy") == 11
    assert vowels_count("abcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()aeiouy1") == 12
    assert vowels_count("abcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()aeiouy1y") == 13
    assert vowels_count("abcdefghijklmnopqrstuv