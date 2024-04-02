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
    return len([c for c in s if c in "aeiou" and c != "y"])

def main():
    import doctest
    doctest.testmod(verbose=True)
    s = raw_input("Enter a string: ")
    print vowels_count(s)

if __name__ == "__main__":
    main()
