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
    vowels = 'aeiouy'
    v_count = 0
    for char in s:
        if char in vowels:
            v_count += 1
    return v_count


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    s = input("Enter a string: ")
    print(vowels_count(s))
