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
	Do not include these tokens in the code: def v ow els _ count (
	"""
    count = 0
    vowels = "aeiouy"
    for c in s:
        if c in vowels:
            count += 1
    return count


def test_vowels_count():
    assert vowels_count("abcde") == 2
    assert vowels_count("ACEDY") == 3
    assert vowels_count("a") == 1
    assert vowels_count("A") == 0
    assert vowels_count("") == 0
    assert vowels_count("abcdey") == 3
    assert vowels_count("aeiou") == 5
    assert vowels_count("AEIOU") == 0
    assert vowels_count("abcdefghijklmnopqrstuvwxyz") == 10
    assert vowels_count("ABCDEFGHIJKLMNOPQRSTUVWXYZ") == 0
    assert vowels_count("abcdefghijklmnopqrstuvwxyzAEIOU") == 15
    assert vowels_count("ABCDEFGHIJKLMNOPQRSTUVWXYZaeiou") == 11


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
    test_vowels_count()

    # print(vowels_count(FIX))
