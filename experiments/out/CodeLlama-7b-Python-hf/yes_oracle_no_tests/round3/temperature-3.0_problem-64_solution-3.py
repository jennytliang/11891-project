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
    # pass
    vowels = ['a', 'e', 'i', 'o', 'u', 'y']
    vowels_count = 0
    for char in s:
        if char in vowels:
            vowels_count += 1
    return vowels_count

def test_vowels_count():
    assert vowels_count('abcde') == 2
    assert vowels_count('ACEDY') == 3
    assert vowels_count('') == 0
    assert vowels_count('a') == 1
    assert vowels_count('aaaaa') == 5
    assert vowels_count('aeiou') == 5
    assert vowels_count('AEIOU') == 5
    assert vowels_count('aEiou') == 5
    assert vowels_count('AEIOU') == 5
    assert vowels_count('y') == 1
    assert vowels_count('Y') == 1
    assert vowels_count('yuyuy') == 5
    assert vowels_count('aeiouy') == 6
    assert vowels_count('aeiouAEIOUy') == 10
    assert vowels_count('aeiouAEIOUyAEIOUy') == 15
    assert vowels_count('aeiouAEIOUyAEIOUyAEIOUy') == 20
    assert vowels_count('AEIOUY') == 6
    assert vowels_count('AEIOU Y') == 6


if __name__ == '__main__':
    import doctest
    doctest.testmod()
    test_vowels_count()

    print(vowels_count('AEIOU Y'))
    print(vowels_count('yuyuy'))
    print(vowels_count('AEIOU Y'))
    print(vowels_count('yuyuy'))
