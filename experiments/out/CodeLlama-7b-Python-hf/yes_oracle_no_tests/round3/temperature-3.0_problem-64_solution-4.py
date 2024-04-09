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


def main():
    for string in [
        "abcde", "ACEDY", "a", "e", "i", "o", "u", "A", "E", "I", "O", "U",
        "y", "Y", " ", "", "a" * 10000000
    ]:
        print("Input: {!r}\nOutput: {!r}".format(string, vowels_count(string)))


if __name__ == "__main__":
    main()
