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
    vowels = {'a': True, 'e': True, 'i': True, 'o': True, 'u': True}
    count = 0
    for c in s:
        c = c.lower()
        if c in vowels:
            count += 1
        elif c == 'y' and s[-1].lower() == 'y':
            count += 1
    return count

def tests():
    import doctest
    doctest.testmod()

if __name__ == '__main__':
    import doctest
