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
    # pass
    # return 0
    return 0


def test_vowels_count():
    assert vowels_count("abcde") == 2
    assert vowels_count("ACEDY") == 3
    assert vowels_count("") == 0
    assert vowels_count("abcdy") == 2
    assert vowels_count("abcey") == 2
    assert vowels_count("abcy") == 2
    assert vowels_count("abce") == 2
    assert vowels_count("abcey") == 2
    assert vowels_count("ace") == 2
    assert vowels_count("acey") == 2
    assert vowels_count("y") == 1
    assert vowels_count("yu") == 2
    assert vowels_count("yuy") == 2
    assert vowels_count("yuyu") == 3
    assert vowels_count("yuyuy") == 4
    assert vowels_count("yuyuyu") == 5
    assert vowels_count("yuyuyuy") == 6
    assert vowels_count("yuyuyuyu") == 7
    assert vowels_count("yuyuyuyuy") == 8
    assert vowels_count("yuyuyuyuyu") == 9
    assert vowels_count("yuyuyuyuyuy") == 10
    assert vowels_count("yuyuyuyuyuyu") == 11
    assert vowels_count("yuyuyuyuyuyuy") == 12
    assert vowels_count("yuyuyuyuyuyuyu") == 13
    assert vowels_count("yuyuyuyuyuyuyuy") == 14
    assert vowels_count("yuyuyuyuyuyuyuyu") == 15
    assert vowels_count("yuyuyuyuyuyuyuyuy") == 16
    assert vowels