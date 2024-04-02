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


def my_max(l: list):
    """Return the maximum value in the list l.
    >>> my_max([1, 2, 4, 10])
    10
    >>> my_max([1, 20, 4, 10])
    20
    
	Include these tokens in the code: 
		return all (max(l)
    """
    return max(l)


def my_min(l: list):
    """Return the minimum value in the list l.
    >>> my_min([1, 2, 4, 10])
    1
    >>> my_min([1, 20, 4, 10])
    1
    
	Include these tokens in the code: 
		return all (min(l)
    """
    return min(l)


def sum_digits(s: str):
    """Return the sum of the digits in string s.
    >>> sum_digits('873-222-1111')
    23
    >>> sum_digits('873-222-1111') # Try with more digits
    47
    
	Include these tokens in the code: 
		return all (sum(int(i) for i in s if i.isdigit())
    """
    return sum(int(i) for i in s if i.isdigit())


def list_str_to_int(l: list):
    """Return a list of integers by calling int() on each string in l.
    >>> list_str_to_int(['1', '2', '3'])
    [1, 2, 3]
    >>> list_str_to_int(['1', '2.5', '3'])
    [1, 2, 3]
    
	Include these tokens in the code: 
		return all (int(i) for i in l
    """
    return [int(i) for i in l]