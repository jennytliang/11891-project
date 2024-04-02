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
	Do not include these tokens in the code: def v ow els _ count (
	"""
    a = s.count("a")+s.count("A")
    e = s.count("e")+s.count("E")
    i = s.count("i")+s.count("I")
    o = s.count("o")+s.count("O")
    u = s.count("u")+s.count("U")
    y = s.count("y")+s.count("Y")
    return a + e + i + o - y


def _test():
    import doctest
    doctest.testmod(verbose=True)
    test_cases = [
            ('abcd', 2),
            ('AEIOU', 5),
            ('', 0),
            ('a eiouy', 4),
            ('AIUEO', 4),
            ('AIUEOh', 5),
            ('AIOUY', 4),
            ('AIOUYh', 4),
            ('AEIOUY', 5),
            (str, (TypeError)),
            (123, (TypeError)),
            (None, (TypeError)),
            ('AEIOUYAEIOU', 7),
    ]

    def _test_func(func, cases):
        fail = 0
        total = len(cases)
        for case in cases:
            inp, ans = case
            try:
                assert func(inp) == ans
            except AssertionError:
                fail += 1
                print ('Test with input %s fail. Expected %s, but got %s!' \
                        % (inp, ans, func(inp)))
        if fail == 0:
            print '%s test passed!' % (total)
    _test_func(vowels_count, test_cases)

if __name__ == "__main__":
    import sys
    if sys.argv[1] == 'ALL':
        _test()
    else:
        _test_func(vowels_count, [tup for tup in test_data])
