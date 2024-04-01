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
    """
    return s.count("a") + s.count("e") + s.count("i") + s.count("o") + s.count("u") + \
            s.count("x") * 2 if s[-1] == "y" else s.count("x")


def main():
    pass


def test():
    tests_correct = 0
    tests_wrong = 0