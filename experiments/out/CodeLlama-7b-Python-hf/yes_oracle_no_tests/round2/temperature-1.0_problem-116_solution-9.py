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
    def count_bin_ones(num):
        """ return binary representation with decimal point of number"""
        return bin(num).strip('0b').replace('1', '1.')
    # count bin value of every number
    binaries = list(map(count_bin_ones, arr))
    # convert them to float and sort in ascending order
    sorted_binaries = sorted(binaries, key=float)
    # use map() to convert float to int
    sorted_bin_ints = map(int, sorted_binaries)
    # finally, use return, join(), and split() to remove the decimal point
    return list(map(int, ' '.join(sorted_bin_ints).split()))


if __name__ == "__main__":

    print(sort_array([1, 5, 2, 3, 4]))
    print(sort_array([]))
    print(sort_array([1, 0, 2, 3, 4]))
    print(sort_array([-2, -3, -4, -5, -6]))
    print(sort_array([1, 10, 2, -20, 30, 4]))
    print(sort_array([0 for _ in range(100)]))


