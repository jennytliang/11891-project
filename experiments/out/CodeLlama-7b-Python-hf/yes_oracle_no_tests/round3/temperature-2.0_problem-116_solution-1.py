def sort_array(arr):
    """
    In this Kata, you have to sort an array of non-negative integers according to
    number of ones in their binary representation in ascending order.
    For similar number of ones, sort based on decimal value.

    It must be implemented like this:
    >>> sort_array([1, 5, 2, 3, 4]) == [1, 2, 3, 4, 5]
    >>> sort_array([-2, -3, -4, -5, -6]) == [-6, -5, -4, -3, -2]
    >>> sort_array([1, 0, 2, 3, 4]) [0, 1, 2, 3, 4]
    
	Include these tokens in the code: from fun ct ools import
	Do not include these tokens in the code: # - ---------------- ---------------- ---------------- ---------------- --------
	"""
    from functools import cmp_to_key

    def compare(a, b):
        if bin(a).count('1') == bin(b).count('1'):
            return a - b
        else:
            return bin(a).count('1') - bin(b).count('1')

    return sorted(arr, key=cmp_to_key(compare))


if __name__ == '__main__':
    print(sort_array([1, 5, 2, 3, 4]))
    print(sort_array([-2, -3, -4, -5, -6]))
    print(sort_array([1, 0, 2, 3, 4]))
