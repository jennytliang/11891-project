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
    pass

def main(attach):
    import doctest, sys

    doctest.testmod(verbose=True)

    # If run with argument -t, touch tmpdir (which is just .. in this case)
    # and make test files named test0.tmp, test1.tmp, etc. which contain
    # 'abcde\n' (i.e., 5 EOF characters), where the number is the test number.
    # See the makefile how to use these to check the program.
    if attach == "-t":
        import os

        os.chdir("..")
        f = open("tmpdir", "w")
        f.close()
        for i in range(10):
            f = open("test%d.tmp" % i, "w")
            print("abcde\n", end="", file=f)
            f.close()

if __name__ == "__main__":
    import sys

    main(sys.argv[1] if len(sys.argv) > 1 else "")
