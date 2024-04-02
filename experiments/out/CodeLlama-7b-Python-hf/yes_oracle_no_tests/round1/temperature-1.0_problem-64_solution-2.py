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
    if s == " ": return 0
    vowels = {"a", "e", "i", "o", "u"}
    s = s.lower()
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    s = input("Enter a word: ")
    print(vowels_count(s))
