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
    vowels = ['a', 'e', 'i', 'o', 'u']
    count = 0
    for c in s:
        if c in vowels:
            if c == 'y' and s.index(c) == len(s) - 1:
                count += 1
            else:
                count += 1
    return count


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    print(vowels_count("abcde"))
    print(vowels_count("ACEDY"))
    print(vowels_count("yAy"))
    print(vowels_count("yAy "))
    print(vowels_count("yAy  "))
    print(vowels_count("yAy  a"))
    print(vowels_count("yAy y"))
    print(vowels_count("yAy y "))
    print(vowels_count("yAy y  "))
    print(vowels_count("yAy y  a"))
