def below_threshold(l: list, t: int):
    """Return True if all numbers in the list l are below threshold t.
    >>> below_threshold([1, 2, 4, 10], 100)
    True
    >>> below_threshold([1, 20, 4, 10], 5)
    False
    
	Include these tokens in the code: return all ( x < t
	"""
    # loop through each value
    # return True if value is less than the threshold

    # pass  # Implement me!!!
    for x in l:
        # break when condition is not met
        if x >= t:
            return False
    return True

print(below_threshold([1, 2, 4, 10], 100))
# True
print(below_threshold([1, 20, 4, 10], 5))
# False   
