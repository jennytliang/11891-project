def sort_array(arr):
    """
    In this Kata, you have to sort an array of non-negative integers according to
    number of ones in their binary representation in ascending order.
    For similar number of ones, sort based on decimal value.

    It must be implemented like this:
    >>> sort_array([1, 5, 2, 3, 4]) == [1, 2, 3, 4, 5]
    >>> sort_array([-2, -3, -4, -5, -6]) == [-6, -5, -4, -3, -2]
    >>> sort_array([1, 0, 2, 3, 4]) [0, 1, 2, 3, 4]
    
	Include these tokens in the code: from fun ct ools import c mp _ to _
	"""
    return sorted(arr, key=cmp_to_key(compare_bits))

def compare_bits(a, b):
    if a == b:
        return 0
    a_ones = count_ones(a)
    b_ones = count_ones(b)
    if a_ones == b_ones:
        return a - b
    return a_ones - b_ones

def count_ones(n):
    count = 0
    while n:
        count += n & 1
        n >>= 1
    return count

if __name__ == '__main__':
    print(sort_array([1, 5, 2, 3, 4]))
    print(sort_array([-2, -3, -4, -5, -6]))
    print(sort_array([1, 0, 2, 3, 4]))
