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
    # pass  # TO DO...
    if s == " ":
        return 0
    if s[-1] == "y":
        return s.count("a") + s.count("e") + s.count("i") + s.count("o") + s.count("u") + s.count("y")
    else:
        return s.count("a") + s.count("e") + s.count("i") + s.count("o") + s.count("u")





def test_vowels_count():
    assert vowels_count("abcde") == 2
    assert vowels_count("ACEDY") == 3
    assert vowels_count("y") == 0
    assert vowels_count("") == 0
    assert vowels_count("aaaaa") == 5


if __name__ == "__main__":
    import doctest
    doctest.testmod()
