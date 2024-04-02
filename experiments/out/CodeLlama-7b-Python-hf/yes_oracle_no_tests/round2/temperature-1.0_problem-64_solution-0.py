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
    pass

from doctest import run_docstring_examples
run_docstring_examples(vowels_count, globals())

if __name__ == "__main__":
    import cProfile
    cProfile.run("vowels_count('vowels_count')", sort="cumulative")
    # run_docstring_examples(vowels_count, globals(), True)
