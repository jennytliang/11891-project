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
	"""
    s = s.lower()
    if s == " ":
        return 0
    count = 0
    for i in s:
        if i in "aeiou":
            count += 1
    return count

def vowels_count_alt(s):
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
	"""
    s = s.lower()
    if s == " ":
        return 0
    count = 0
    for i in s:
        if i in "aeiou":
            count += 1
    return count

def vowels_count_alt2(s):
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
	"""
    s = s.lower()
    if s == " ":
        return 0
    count = 0
    for i in s:
        if i in "aeiou":
            count += 1
    return count

def vowels_count_alt3(s):
    """Write a function vowels_count which takes a string representing
    a