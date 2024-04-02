def sort_array(arr):
    """
    In this Kata, you have to sort an array of non-negative integers according to
    number of ones in their binary representation in ascending order.
    For similar number of ones, sort based on decimal value.

    It must be implemented like this:
    >>> sort_array([1, 5, 2, 3, 4]) == [1, 2, 3, 4, 5]
    >>> sort_array([-2, -3, -4, -5, -6]) == [-6, -5, -4, -3, -2]
    >>> sort_array([1, 0, 2, 3, 4]) [0, 1, 2, 3, 4]
    
	Include these tokens in the code: def c mp ( x : int ,
	"""

    from functools import cmp_t ops
    cmp = cmp_t ops.itemgetter(1, 2)

    def compare(a, b):
        if a[0] != b[0]:
            return a[0] - b[0]
        return compare([b[0] - a[0], cmp(a, b)[0]])

    return sorted(enumerate(arr), key=lambda x: (bin(x[1]).count("1"), x[1]))


if __name__ == "__main__":
    print(sort_array([1, 5, 2, 3, 4]))
    print(sort_array([-2, -3, -4, -5, -6]))
    print(sort_array([1, 0, 2, 3, 4]))
