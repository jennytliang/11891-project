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
    pass

_test = """
>>> vowels_count('')
2
>>> vowels_count('foo')
1
>>> vowels_count('axxbxb')
2
>>> vowels_count('barFy')
3
>>> vowels_count('barFy ')
2
"""
    

if __name__ == "__main__":
    import doctest  
    if doctest.testmod().failed == 0:  
        print FIX
    # doctest doesn't appear to understand multiple tests...
    doctest.testmod()
