def sort_array(arr):
    """
    In this Kata, you have to sort an array of non-negative integers according to
    number of ones in their binary representation in ascending order.
    For similar number of ones, sort based on decimal value.

    It must be implemented like this:
    >>> sort_array([1, 5, 2, 3, 4]) == [1, 2, 3, 4, 5]
    >>> sort_array([-2, -3, -4, -5, -6]) == [-6, -5, -4, -3, -2]
    >>> sort_array([1, 0, 2, 3, 4]) [0, 1, 2, 3, 4]
    
	Include these tokens in the code: c mp
	Do not include these tokens in the code: compare _ to
	"""

    from functools import cmp_to_key

 
    def compare_by_ones_number(a, b):
        """
        Compare a and b based on number of ones in binary representation
        """
        def count_ones(n):
            """
            Count number of ones in binary representation
            """
            return bin(n).count('1')

        if count_ones(a) == count_ones(b):
            return a - b
        else:
            return count_ones(b) - count_ones(a)

    return sorted(arr, key=cmp_to_key(compare_by_ones_number))


if __name__ == "__main__":
    print(sort_array([1, 5, 2, 3, 4]))
    print(sort_array([-2, -3, -4, -5, -6]))
    print(sort_array([1, 0, 2, 3, 4]))
