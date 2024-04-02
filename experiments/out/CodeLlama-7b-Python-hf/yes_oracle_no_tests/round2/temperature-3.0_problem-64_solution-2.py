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
    count = 0
    for c in s:
        if c in 'aeiou':
            count += 1
        elif c == 'y':
            if s[-1] == 'y':
                count += 1
    return count

def test_vowels_count():
    """Write your own test cases.
    """
    assert vowels_count("abcde") == 2
    assert vowels_count("ACEDY") == 3
    assert vowels_count("") == 0

if __name__ == "__main__":
    test_vowels_count()
