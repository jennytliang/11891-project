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

    pass


def test_vowels_count():

    assert vowels_count("abcde") == 2
    assert vowels_count("ACEDY") == 3
    assert vowels_count("yxz") == 0
    assert vowels_count("") == 0
    assert vowels_count("aeiou") == 5
    assert vowels_count("aiueo") == 5
    assert vowels_count("AEIOU") == 5
    assert vowels_count("aiyoo") == 4
    assert vowels_count("aiyuy") == 3
    assert vowels_count("aiyuy") == 3
    assert vowels_count("aiyuyu") == 4
    assert vowels_count("aiyuyuu") == 5
    assert vowels_count("a") == 1
    assert vowels_count("e") == 1
    assert vowels_count("i") == 1
    assert vowels_count("o") == 1
    assert vowels_count("u") == 1
    assert vowels_count("y") == 0
    assert vowels_count(" ") == 0
    assert vowels_count("aeiouy") == 5
    assert vowels_count("aeiouy ") == 5
    assert vowels_count("aeiouyaiyoo") == 8
    assert vowels_count("aeiouyaiyuy") == 7
    assert vowels_count("aeiouyaiyuyu") == 8
    assert vowels_count("aeiouyaiyuyuu") == 9
    assert vowels_count("aeiouyaiyuyuyu") == 8
    assert vowels_count("aeiouyaiyuyuyuu") == 9
    assert vowels_count("aeiouyaiyuyuyuyu") == 8
    assert vowels_count("aei