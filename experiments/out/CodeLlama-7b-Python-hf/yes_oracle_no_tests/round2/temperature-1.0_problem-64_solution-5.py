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
    assert vowels_count("") == 0
    assert vowels_count("qwerty") == 0
    assert vowels_count("y") == 0
    assert vowels_count("a") == 1
    assert vowels_count("A") == 0
    assert vowels_count("aeiou") == 5
    assert vowels_count("AEIOU") == 0
    assert vowels_count("aeiouAEIOU") == 10
    assert vowels_count("aeiouAEIOUaeiou") == 20
    assert vowels_count("aeiouaeiouAEIOUaeiouAEIOU") == 20
    assert vowels_count("abcdefghijklmnopqrstuvwxyz") == 20
    assert vowels_count("ABCDEFGHIJKLMNOPQRSTUVWXYZ") == 0
    assert vowels_count("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ") == 40


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    test_vowels_count()
