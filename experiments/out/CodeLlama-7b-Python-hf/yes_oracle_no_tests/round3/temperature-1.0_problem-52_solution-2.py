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



def count_below_threshold(l: list, t: int):
    """Return the number of elements in the list l that are below threshold t.
    >>> count_below_threshold([1, 2, 4, 10, 0], 5)
    3
	Include these tokens in the code: return 
    """
    count = 0
    for x in l:
        if x < t:
            count += 1
    return count



def sum_below_threshold(l: list, t: int):
    """Return the sum of elements in the list l that are below threshold t.
    >>> sum_below_threshold([1, 2, 4, 10, 0], 5)
    7
    >>> sum_below_threshold([1, 20, 4, 10, 0], 5)
    7
    
	Include these tokens in the code: return
    """
    sum = 0
    for x in l:
        if x < t:
            sum += x
    return sum



def average_below_threshold(l: list, t: int):
    """Return the average of elements in the list l that are below threshold t.
    >>> average_below_threshold([1, 2, 4, 10, 0], 5)
    1.4
    >>> average_below_threshold([1, 20, 4, 10, 0], 5)
    1.4
    
	Include these tokens in the code: return
    """
    sum = 0
    count = 0
    for x in l:
        if x < t:
            sum += x
            count += 1
    return sum / count
