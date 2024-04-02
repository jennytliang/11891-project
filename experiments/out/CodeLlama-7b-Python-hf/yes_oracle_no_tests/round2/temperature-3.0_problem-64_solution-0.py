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
    return sum(
        s.count(c)
        for c in "aeiouy"
        if not s.endswith("y") or c != "y"
    )

# print(vowels_count("abcde"))
# print(vowels_count("ACEDY"))

def test_vowels_count():
    assert vowels_count("abcde") == 2
    assert vowels_count("ACEDY") == 3
    assert vowels_count("yuyuy") == 4
    assert vowels_count("yuyuyu") == 5
    assert vowels_count("yuyuyuo") == 5
    assert vowels_count("yuyuyuu") == 6
    assert vowels_count("yuyuyuoo") == 6
    assert vowels_count("yuyuyuuu") == 7
    assert vowels_count("yuyuyuooo") == 7
    assert vowels_count("yuyuyuuuu") == 8
    assert vowels_count("yuyuyuoooo") == 8
    assert vowels_count("yuyuyuuuuu") == 9
    assert vowels_count("yuyuyuooooo") == 9
    assert vowels_count("yuyuyuuuuuu") == 10
    assert vowels_count("yuyuyuoooooo") == 10
    assert vowels_count("yuyuyuuuuuuu") == 11
    assert vowels_count("yuyuyuooooooo") == 11
    assert vowels_count("yuyuyuuuuuuuu") == 12
    assert vowels_count("yuyuyuoooooooo") == 12
    assert vowels_count("yuyuyuuuuuuuuu") == 13
    assert vowels_count("yuyuyuooooooooo") ==