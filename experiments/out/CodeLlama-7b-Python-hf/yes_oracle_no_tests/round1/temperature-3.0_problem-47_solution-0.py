def median(l: list):
    """Return median of elements in the list l.
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    
	Include these tokens in the code: sorted _ l
	"""
    sorted_l = sorted(l)
    length = len(l)
    if length % 2 == 0:
        return (sorted_l[length // 2 - 1] + sorted_l[length // 2]) / 2
    else:
        return sorted_l[length // 2]


print("l = [3, 1, 2, 4, 5], median(l) = 3:", median([3, 1, 2, 4, 5]))
print("l = [-10, 4, 6, 1000, 10, 20], median(l) = 15:", median([-10, 4, 6, 1000, 10, 20]))
print("l = [1, 1, 1, 1, 1], median(l) = 1:", median([1, 1, 1, 1, 1]))
print("l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], median(l) = 5.5:", median([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
