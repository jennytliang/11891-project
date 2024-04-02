def below_threshold(l: list, t: int):
    """Return True if all numbers in the list l are below threshold t.
    >>> below_threshold([1, 2, 4, 10], 100)
    True
    >>> below_threshold([1, 20, 4, 10], 5)
    False
    
	Include these tokens in the code: return all ( x < t
	"""

    for i in range(len(l)):
        if l[i] < t:
            return True
    return False



def odd_numbers(n):
    """Return a list of the first n odd numbers.
    >>> odd_numbers(5)
    [1, 3, 5, 7, 9]
    """
    result = []
    for i in range(1, n + 1, 2):
        result.append(i)
    return result



def make_summer(a):
    def summer(m):
        return a + m
    return summer

fce = make_summer(6)
print(fce(4))