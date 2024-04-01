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
    
	Include these tokens in the code:  if s == " ": return
	Do not include these tokens in the code: v ow els = [' a ', ' e
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
    """
    vowels = ['a', 'e', 'i', 'o', 'u', 'y']
    count = 0
    for letter in s:
        if letter in vowels:
            count += 1
    return count


# -----------------------------------------------------------------------------
# Coding
# -----------------------------------------------------------------------------
if __name__ == '__main__':
    with Expect({
        str: int,
    }):
        vowels_count('')
    with Expect({
        str: int,
    }):
        vowels_count(' ')
    with Expect({
        str: int,
    }):
        vowels_count('aeiou')
    with Expect({
        str: int,
    }):
        vowels_count('aeiouy')
    with Expect({
        str: int,
    }):
        vowels_count('aeiouy ')
    with Expect({
        str: int,
    }):
        vowels_count('AEIOU')
    with Expect({
        str: int,
    }):
        vowels_count('AEIOUY')
    with Expect({
        str: int,
    }):
        vowels_count('AEIOUY ')
    with Expect({
        str: int,
    }):
        vowels_count('aeiouy')
    with Expect({
        str: int,
    }):
        vowels_count('AEIOUY')
    with Expect({
        str: int,
    }):
        vowels_count('AEIOUY ')
    with Expect({
        str: int,
    }):
        vowels_count('AEIOUY ')
    with Expect({
        str: int,
    }):
        vowels_count('AEIOUY ')
    with Expect({
        str: int,
    }):
        vowels_count('AEIOUY ')
    with Expect({
        str: int,
    }):