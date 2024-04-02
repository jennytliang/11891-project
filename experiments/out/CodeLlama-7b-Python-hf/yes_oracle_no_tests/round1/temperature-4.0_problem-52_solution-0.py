def below_threshold(l: list, t: int):
    """Return True if all numbers in the list l are below threshold t.
    >>> below_threshold([1, 2, 4, 10], 100)
    True
    >>> below_threshold([1, 20, 4, 10], 5)
    False
    
	Include these tokens in the code: return all ( x < t
	"""

    for x in l:
        if x < t:
            return True
    return False


def only_strings(l: list, t: str):
    """Return True if all elements in the list l are of type str.
    >>> only_strings(["a", "b", "c"], "d")
    True
    >>> only_strings([1, "b", "c"], "d")
    False
    
	Include these tokens in the code: return all ( isinstance(x, str)
	"""

    for x in l:
        if not isinstance(x, str):
            return False
    return True


def sum_digits(s: str):
    """Return the sum of all digits in string s.
    >>> sum_digits("hello")
    0
    >>> sum_digits("there")
    8
    >>> sum_digits("123abc")
    6
    >>> sum_digits("7543")
    22
    
	Include these tokens in the code: return sum(int(c) for c in s if c.isdigit())
	"""

    return sum(int(c) for c in s if c.isdigit())


def without_vowels(s: str):
    """Return a string that is the same as s, except that all 'a', 'e', 'i',
    'o', and 'u' have been removed.
    >>> without_vowels("Hello!")
    Hll!
    >>> without_vowels("The quick brown fox jumped over the lazy dog.")
    Th qck brwnfx jmpped vr th lzy dg.
    
	Include these tokens in the code: replace all (c in s if not c.lower() in 'aeiou')
	"""

    return "".join(c for c in s if not c.lower() in 'aeiou')


def has_no_e(s: str):
    """Return True if the given string has no 'e' characters in it.
    >>> has_no_e("hello")
    False
