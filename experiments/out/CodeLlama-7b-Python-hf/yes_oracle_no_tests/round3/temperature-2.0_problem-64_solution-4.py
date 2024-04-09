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
    
    vowels = 'aeiouy'
    vowel_count = 0
    for c in s:
        if c in vowels:
            vowel_count += 1

    return vowel_count

def vowels_count_alt(s):
    """An alternate solution that doesn't use a loop.

    >>> vowels_count("abcde")
    2
    >>> vowels_count("ACEDY")
    3
    """
    return s.count('a') + s.count('e') + s.count('i') + s.count('o') + s.count('u') + s.count('y')


def vowels_count_alt2(s):
    """An alternate solution that doesn't use a loop.

    >>> vowels_count("abcde")
    2
    >>> vowels_count("ACEDY")
    3
    """
    vowels = 'aeiouy'
    vowel_count = 0
    for c in vowels:
        vowel_count += s.count(c)

    return vowel_count


def vowels_count_alt3(s):
    """An alternate solution that doesn't use a loop.

    >>> vowels_count("abcde")
    2
    >>> vowels_count("ACEDY")
    3
    """
    vowels = 'aeiouy'
    vowel_count = 0
    for c in s:
        if c in vowels:
            vowel_count += 1

    return vowel_count


def vowels_count_alt4(s):
    """An alternate solution that doesn't use a loop.

    >>> vowels_count("abcde")
    2
    >>> vowels_count("ACEDY")
    3
    """
    vowels = 'aeiouy'
    vowel_count = 0
    for c in s:
        if c in vowels:
            vowel_