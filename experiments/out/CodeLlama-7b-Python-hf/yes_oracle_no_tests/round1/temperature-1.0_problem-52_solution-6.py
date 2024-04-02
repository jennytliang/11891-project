def below_threshold(l: list, t: int):
    """Return True if all numbers in the list l are below threshold t.
    >>> below_threshold([1, 2, 4, 10], 100)
    True
    >>> below_threshold([1, 20, 4, 10], 5)
    False
    
	Include these tokens in the code: return all ( x < t
	"""
    for x in l:
      pass
      # FILL IN MISSING CODE AFTER THIS LINE
      # BEGIN PROBLEM 3
    return t
    # END PROBLEM 3

if __name__ == "__main__":
    import doctest
    doctest.testmod()