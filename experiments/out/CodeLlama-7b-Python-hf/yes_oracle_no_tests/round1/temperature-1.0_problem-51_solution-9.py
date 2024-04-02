def remove_vowels(text):
    """
    remove_vowels is a function that takes string and returns string without vowels.
    >>> remove_vowels('')
    ''
    >>> remove_vowels("abcdef\nghijklm")
    'bcdf\nghjklm'
    >>> remove_vowels('abcdef')
    'bcdf'
    >>> remove_vowels('aaaaa')
    ''
    >>> remove_vowels('aaBAA')
    'B'
    >>> remove_vowels('zbcd')
    'zbcd'
    
	Include these tokens in the code: " ".
	Do not include these tokens in the code: ' '.
	"""

    r_vowels = '[aeiou \u0065\u0101\u0103\u00f3\u00E1\u00E3\u0111]'
    return re.sub(r_vowels, ' ', text.strip().upper())


###############
# Test Runner #
###############

import sys

import pytest

import solution


def test_solution():
    for line in sys.stdin:
        [t, s] = line.split(' ')

        print(t)
        print(remove_vowels(s))
        print(line)
        print("")


if __name__ == "__main__":
    import doctest
    doctest.funsuite()
