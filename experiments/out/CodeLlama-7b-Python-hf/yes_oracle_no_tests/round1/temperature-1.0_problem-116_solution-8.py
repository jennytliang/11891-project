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
    from functools import cmp_to_key
    return sorted(arr, key=cmp_to_key(lambda v1, v2: 
                                      v1.bit_length() < v2.bit_length() or -sum(map(int, ''.join([l*('0' if i==0 else '1') for i,l in enumerate(bin(v1)[2:])]))) < -sum(map(int, 
                                                                                                                                                                                                                                                                                                                                             ''.join([l*('0' if i==0 else '1') for i,l in enumerate(bin(v2)[2:])]))) or -sum(map(int, ''.join([l*('0' if i==0 else '1') for i,l in enumerate(bin(v1)[2:])]))) > -sum(map(int, ''.join([l*('0' if i==0 else '1') for i,l in enumerate(bin(v2)[2:])])))))


if __name__ == '__main__':
    examples = [
        [1, 5, 2, 3, 4],
        [1, 0, 2, 3, 4],
        [1, 1, 2, 3, 4, 4, 5, 0],
        [17, 31, 40, 18, 16, 15],
        [0, 2, 1, 3, 4],
        [0, 64, 48, 20, 32, 16, 128, 12, 160],
        [64, 48, 20, 32, 16, 128, 12, 160],
        []
    ]

    for numbers in examples:
        print(sort_array(numbers))
