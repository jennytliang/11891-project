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

    # YOUR CODE HERE
    return 0


def vowels_count_with_counts(s):
    """Write a function vowels_count_with_counts which takes a string representing
    a word as input and returns a dictionary with the keys as vowels and the
    values as the count of vowels. Vowels in this case are 'a', 'e', 'i', 'o', 'u'.
    Here, 'y' is also a vowel, but only when it is at the end of the given word.

    Example:
    >>> vowels_count_with_counts("abcde")
    {'a': 1, 'e': 1, 'i': 0, 'o': 0, 'u': 0}
    >>> vowels_count_with_counts("ACEDY")
    {'a': 1, 'e': 1, 'i': 0, 'o': 1, 'u': 0}
    >>> vowels_count_with_counts("ACED")
    {'a': 1, 'e': 1, 'i': 0, 'o': 0, 'u': 0}
    >>> vowels_count_with_counts("Yo, he said")
    {'a': 1, 'e': 1, 'i': 0, 'o': 1, 'u': 0}
    
	Do not include these tokens in the code: def v ow els _ count (
	"""

    # YOUR CODE HERE
    return {}


def vowels_count_with_counts_and_sets(s):
    """Write a function vowels_count_with_counts_and_sets which takes a string representing
    a word as input and returns a dictionary with the keys as vowels and the
    values as the count of vowels. Vowels in this case are 'a', 'e', 'i', 'o', 'u'.
    Here, 'y' is also a vowel, but only when it is at the end of the given word.

   