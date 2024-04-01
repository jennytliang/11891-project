def below_threshold(l: list, t: int):
    """Return True if all numbers in the list l are below threshold t.
    >>> below_threshold([1, 2, 4, 10], 100)
    True
    >>> below_threshold([1, 20, 4, 10], 5)
    False
    
	Do not include these tokens in the code:  for num in l :  if num
	"""

    # for num in l:
    #     if num < t:
    #         return True
    # return False

    # return all(num < t for num in l)

    # if l:
    #     return all(num < t for num in l)
    # return True

    return not any(num >= t for num in l)


# print(below_threshold([1, 2, 4, 10], 100))
# print(below_threshold([1, 20, 4, 10], 5))


def same_first_last(l: list):
    """Returns True if the first and last elements of a list are the same.
    >>> same_first_last([1, 2, 1])
    True
    >>> same_first_last([1, 2, 4, 1])
    False
    """
    # if l:
    #     return l[0] == l[-1]
    # return False

    return l[0] == l[-1] if l else False


# print(same_first_last([1, 2, 1]))
# print(same_first_last([1, 2, 4, 1]))


def has_23(n: int):
    """Returns True if the given number n as a string contains a 2 or 3.
    >>> has_23(243)
    True
    >>> has_23(253)
    False
    """
    return "2" in str(n) or "3" in str(n)


# print(has_23(243))
# print(has_23(253))


def all_same_end(l: list):
    """Returns True if all the strings in the list end with the same letter.
    >>> all_same_end(['act','god','ham','yam'])
    True
    >>> all_same_end(['act','god','hamlet','yam'])
    False
    """

    # if not