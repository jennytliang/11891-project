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
    return sum(1 for c in s if c in 'aeiouy' and c != 'y' or c == s[-1] == 'y')


def test_vowels_count():
    assert vowels_count("abcde") == 2
    assert vowels_count("ACEDY") == 3
    assert vowels_count("abcdey") == 3
    assert vowels_count("") == 0
    assert vowels_count("y") == 1
    assert vowels_count("aei") == 3
    assert vowels_count("aeiou") == 5
    assert vowels_count("aeiouy") == 6
    assert vowels_count("yu") == 2
    assert vowels_count("aeiouaeiouy") == 8
    assert vowels_count("aeiouaeiouaeiouy") == 12
    assert vowels_count("aeiouaeiouaeiouaeiouy") == 16
    assert vowels_count("a") == 1
    assert vowels_count("b") == 0
    assert vowels_count("c") == 0
    assert vowels_count("d") == 0
    assert vowels_count("e") == 1
    assert vowels_count("f") == 0
    assert vowels_count("g") == 0
    assert vowels_count("h") == 0
    assert vowels_count("i") == 1
    assert vowels_count("j") == 0
    assert vowels_count("k") == 0
    assert vowels_count("l") == 0
    assert vowels_count("m") == 0
    assert vowels_count("n") == 0
    assert vowels_count("o") == 1
    assert vowels_count("p") == 0
    assert vowels_count("q") == 0
    assert vowels_