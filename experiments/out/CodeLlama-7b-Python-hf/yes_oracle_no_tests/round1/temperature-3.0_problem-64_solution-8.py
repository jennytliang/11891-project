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

    # pass # TO DO ...
    count = 0
    for letter in s:
        if letter == 'a' or letter == 'e' or letter == 'i' or letter == 'o' or letter == 'u':
            count += 1
    return count


def test_cases():
    assert vowels_count("abcde") == 2
    assert vowels_count("ACEDY") == 3
    assert vowels_count("aeiou") == 5
    assert vowels_count("AaEeIiOoUuYy") == 8
    assert vowels_count("") == 0
    assert vowels_count(" ") == 0
    assert vowels_count("aeiouy") == 5
    assert vowels_count("aeiouyy") == 6
    assert vowels_count("yAeEiIoOuUy") == 8
    print("Test Success!")


if __name__ == "__main__":
    test_cases()

