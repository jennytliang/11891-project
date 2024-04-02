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
    vowels = 'aeiou'
    if s == " ":
        return 0
    return len([x for x in s if x in vowels])


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    print(vowels_count("abcde"))
    print(vowels_count("ACEDY"))
    print(vowels_count("y"))
    print(vowels_count(" "))
    print(vowels_count(""))
    print(vowels_count("abcdefghijklmnopqrstuvwxyz"))
