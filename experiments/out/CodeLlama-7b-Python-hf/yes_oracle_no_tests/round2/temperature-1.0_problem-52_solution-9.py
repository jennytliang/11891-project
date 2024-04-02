def below_threshold(l: list, t: int):
    """Return True if all numbers in the list l are below threshold t.
    >>> below_threshold([1, 2, 4, 10], 100)
    True
    >>> below_threshold([1, 20, 4, 10], 5)
    False
    
	Include these tokens in the code: return all ( x < t
	"""
    for num in l:
        if num >= t:
            return False # if one number is greater than or equal to threshold
    return True # if none are greater than or equal to threshold

def same_first_and_last(l: list):
    """Return True if the first and last numbers of l are the same.

    >>> same_first_and_last([1, 2, 1])
    True
    >>> same_first_and_last([1, 2, 1, 3, 1])
    True
    >>> same_first_and_last([2, 1, 2])
    False

    This function should use only two lines.
    """
    return l[0] == l[-1]

def biggest(a: int, b: int, c: int):
    """Return the biggest out of a, b, and c.

    >>> biggest(1, 5, 2)
    5
    >>> biggest(4, 3, 5)
    5
    >>> biggest(2, 0, 1)
    2

	Use a line with no newlines in it.
	The simplest way to do this is to use tuple unpacking.
	First try using the lines
	    if a >= b and a >= c:
	        return a
	    if b >= a and b >= c:
	        return b
	    return c
	Then eliminate redundancies.
	"""
    return max(a, b, c)

def all_same_symbol(w: str):
    """Return True if all the characters in w are the same.

    >>> all_same_symbol("hey")
    False
    >>> all_same_symbol("hi")
    True
    >>> all_same_symbol("aaa")
    True

	To get rid of the redundancies, start with the
    all-False case. Then if one character does not match, the
    function is False, and you don't need to check any more chars.
    """
    if len(w) < 2:
        return True
    return w[0] ==