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
    return (s.count("a") + s.count("e") + s.count("i") + s.count("o") +
            s.count("u") + s.count("y"))

def test_fucn(got, expected):
    if got == expected:
        mark = "OK"
    else:
        mark = "X"
    print(f'{mark} got: {got} expected: {expected}')


mystr = input("Enter string here:")
test_fucn(vowels_count(mystr), len(mystr) // len("y"))
