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
    return 0


def vowels_count_alt(s):
    """An alternate solution."""
    return s.count("a") + s.count("e") + s.count("i") + s.count("o") + s.count("u")


def test_one(func, s, expected):
    result = func(s)
    if result == expected:
        print("Test passed!")
    else:
        print("Test failed!")
    print("The correct result is:", expected)
    print("Your result is    :", result)
    print()


def test_cases():
    test_one(vowels_count, "abcde", 2)
    test_one(vowels_count, "ACEDY", 3)
    test_one(vowels_count_alt, "abcde", 2)
    test_one(vowels_count_alt, "ACEDY", 3)


def main():
    test_cases()


if __name__ == "__main__":
    main()
