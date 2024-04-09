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
    
	Include these tokens in the code: if s == " ":
	Do not include these tokens in the code: def v ow els _ count (
	"""
    vowels = "aeiou"
    vowels_count = 0
    for letter in s:
        if letter in vowels:
            vowels_count += 1
    return vowels_count

def test_vowels_count():
    assert vowels_count("abcde") == 2
    assert vowels_count("ACEDY") == 3
    assert vowels_count("abcdey") == 3
    assert vowels_count("") == 0
    assert vowels_count("a b c d e") == 5
    assert vowels_count("y") == 0
    assert vowels_count("AEIOU") == 5
    assert vowels_count("aeiou") == 5
    assert vowels_count("AEIOUY") == 6
    assert vowels_count("aeiouy") == 6
    assert vowels_count("aeiouAEIOU") == 10
    assert vowels_count("yAEIOUY") == 6
    assert vowels_count("yaeiouy") == 6
    assert vowels_count("yAEIOUaeiou") == 12
    assert vowels_count("!") == 0
    assert vowels_count("!a") == 1
    assert vowels_count("!aeiou") == 5
    assert vowels_count("!aeiouy") == 6
    assert vowels_count("!aeiouAEIOUy") == 12
    assert vowels_count("!aeiouAEIOUY") == 12
    assert vowels_count("!aeiouAEIOUyAEIOU") == 20
    assert vowels_count("!AEIOUY") == 6
    assert vowels_count("!AEIOUaeiou") == 12
    assert vowels_count("!AEIOUaeiouAEIOUaeiouAEIOUaeiou