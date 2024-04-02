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
    assert type(s) == str
    if s == "":
        return 0
    vowels = "aiouAEIOU"
    v_count = 0
    for i in range(len(s)):
        if s[i] in vowels:
            v_count += 1
        elif s[i] == "y":
            if s[i + 1] not in vowels:
                v_count += 1
    return v_count


def vowels_count_plus(s):
    """Here is an alternate answer by John Cooke.
    """
    if s == "" or s == None:
        return 0
    vowels = "aiou"
    is_last_y_vowel = False
    vowels_count = 0
    for i in range(len(s)):
        char = s[i].lower()
        if char in vowels:
            vowels_count += 1
        elif char == 'y':
            is_last_y_vowel = True
    if is_last_y_vowel:
        vowels_count += 1
    return vowels_count

def vowels_count_best(s):
    """The answer by John Cooke is much simpler than both our methods.
    """
    vowels = "aiou"
    is_last_y_vowel = False
    count = sum(s[0] in vowels
                or s[0:2] in ["ya", "ye"] # John Cooke addition
                for s in s.split("y")
    )
    return count


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
