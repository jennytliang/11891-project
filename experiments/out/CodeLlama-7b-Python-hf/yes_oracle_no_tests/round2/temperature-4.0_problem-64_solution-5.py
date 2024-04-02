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
    vowels = 'aeiouAEIOU'
    count = 0
    for c in s:
        if c in vowels:
            count += 1
    return count


def test_vowels_count():
    assert vowels_count("abcde") == 2
    assert vowels_count("ACEDY") == 3
    assert vowels_count("ACEDYy") == 4
    assert vowels_count("") == 0
    assert vowels_count("y") == 1
    assert vowels_count("a") == 1
    assert vowels_count("A") == 1
    assert vowels_count("yA") == 2
    assert vowels_count("Ay") == 2
    assert vowels_count("AyA") == 3
    assert vowels_count("AyAy") == 4
    assert vowels_count("AyAyA") == 5
    assert vowels_count("AyAyAy") == 6
    assert vowels_count("AyAyAyA") == 7
    assert vowels_count("AyAyAyAy") == 8
    assert vowels_count("AyAyAyAyA") == 9
    assert vowels_count("AyAyAyAyAy") == 10
    assert vowels_count("AyAyAyAyAyA") == 11
    assert vowels_count("AyAyAyAyAyAy") == 12
    assert vowels_count("AyAyAyAyAyAyA") == 13
    assert vowels_count("AyAyAyAyAyAyAy") == 14
    assert vowels_count("AyAyAyAyAyAyAyA") == 15


if __name__ == "__main__":
    import doct