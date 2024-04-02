def below_threshold(l: list, t: int):
    """Return True if all numbers in the list l are below threshold t.
    >>> below_threshold([1, 2, 4, 10], 100)
    True
    >>> below_threshold([1, 20, 4, 10], 5)
    False
    
	Include these tokens in the code: return all ( x < t
	"""
    for x in l:
        if x >= t:
            return False
    return True


def only_strings(l: list, t: str):
    """Return a list with only strings.
    >>> only_strings(["Hello", 2, "Bye"], "str")
    ['Hello', 'Bye']
    """
    return [x for x in l if type(x) == str]


def has_seven(n: int):
    """Return whether n has a 7 in it.
    >>> has_seven(17)
    True
    >>> has_seven(3)
    False
    """
    return "7" in str(n)


def large_diff(l: list):
    """Return the largest difference between two consecutive numbers in l.
    >>> large_diff([10, 3, 5, 6])
    7
    """
    return max([abs(l[i] - l[i + 1]) for i in range(len(l) - 1)])


def sum_digits(s: str):
    """Return the sum of the digits in s.
    >>> sum_digits("7382993")
    36
    >>> sum_digits("12345")
    15
    """
    return sum([int(x) for x in s])


def has_repeated_digits(s: str):
    """Return whether s has two or more repeated digits.
    >>> has_repeated_digits("12345")
    False
    >>> has_repeated_digits("12344")
    True
    """
    return len(set(s)) < len(s)


def has_age(s: str):
    """Return whether the string s represents an age in years.
    An age in years is a number in the range 0..110.
    >>> has_age("90")
    True
    >>> has_age("-1")
    False
    >>> has_age("120")
   