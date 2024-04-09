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
    
	Include these tokens in the code: if s
	Do not include these tokens in the code: def v ow els _ count (
	"""
    # pass
    count = 0
    for letter in s:
        if letter in "aeiou":
            count += 1
    return count

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
    
	Include these tokens in the code: if s
	Do not include these tokens in the code: def v ow els _ count (
	"""
    count = 0
    for letter in s:
        if letter in "aeiou":
            count += 1
        elif letter == 'y' and s.index(letter) == len(s) - 1:
            count += 1
    return count

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
    
	Include these tokens in the code: if s
	Do not include these tokens in the code: def v ow els _ count (
	"""
    count = 0
    for letter in s:
        if letter in "aeiou":
            count += 1
        elif letter == 'y' and s.index(letter) == len(s) - 1:
            count += 1
    return count

def vowels