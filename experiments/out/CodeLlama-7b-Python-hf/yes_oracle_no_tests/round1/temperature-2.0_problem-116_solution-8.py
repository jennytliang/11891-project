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
    # The idea is to use the fact that 10001010100010001000000000000000
    # is lexicographically greater than 01000000000000000000000000000000
    # to create a key for the sort.
    
    # The key is to find the number of ones in the binary representation
    # of the number.
    
    # To do this, we convert the number to binary, and count the number
    # of ones.
    # For example:
    # 10001010100010001000000000000000
    # 000000000000000000000000000110101
    
    # To find the number of ones, we can use the fact that the sum of
    # the digits is equal to the number of ones.
    
    # The key is to find the number of digits in the binary representation
    # of the number.
    
    # To do this, we can divide the number by 2, and keep dividing by 2 until
    # the number is 0.
    # We can then count the number of times we divided by 2.
    # This is the number of digits in the binary representation of the number.
    
    # To find the number of ones, we can sum the digits.
    
    # To find the number of digits, we can use the fact that the sum of the
    # digits is equal to the number of ones.
    
    # We can use this to sort the array, by using the key function.
    
    return sorted(arr, key=lambda x: (bin(x).count('1'), x))

if __name__ == '__main__':
    import doctest
    doctest.testmod()
