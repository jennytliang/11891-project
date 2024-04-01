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
    
    vowels = 'aeiou'
    return sum([s.count(v) for v in vowels])


def test_vowels_count():
    assert vowels_count('abcde') == 2
    assert vowels_count('ACEDY') == 3
    assert vowels_count('') == 0
    assert vowels_count('y') == 0
    assert vowels_count('a') == 1
    assert vowels_count('b') == 0
    assert vowels_count('ab') == 1
    assert vowels_count('ababab') == 3
    assert vowels_count('aabbab') == 3
    assert vowels_count('abcdefghijklmnopqrstuvwxyz') == 20


if __name__ == '__main__':
    test_vowels_count()
