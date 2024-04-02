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
    return 0

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    import re
    import random
    import string

    print(vowels_count("abcde"))
    print(vowels_count("ACEDY"))
    print(vowels_count("abcdey"))
    print(vowels_count("ace"))
    print(vowels_count("y"))
    print(vowels_count(""))

    for _ in range(1000):
        s = "".join(random.choice(string.ascii_letters) for _ in range(10))
        count = len(re.findall("[aeiouy]", s, re.IGNORECASE))
        assert vowels_count(s) == count
