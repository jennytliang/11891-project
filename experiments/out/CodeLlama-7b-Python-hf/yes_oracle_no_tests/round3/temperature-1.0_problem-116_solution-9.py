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
    # This solution is based on the idea that we can use Python's list.sort()
    # method, but with a custom sort function that sorts the array in the
    # desired way.  The custom sort function must return a negative number if
    # the first element is less than the second element, a positive number if
    # the first element is greater than the second element, and zero if the
    # two elements are equal.  To sort in descending order, we just negate the
    # custom sort function.
    #
    # We can use Python's built-in function cmp_to_key() to convert a custom
    # sort function into a custom key function.  We can then use the list.sort()
    # method with the key parameter to sort the array using the custom key
    # function.
    #
    # The custom sort function is based on the idea that we can convert a
    # number into a string representation of its binary value by using the
    # format() method and the "b" format specifier.  We can then count the
    # number of ones in the binary representation by using the count()
    # method.  We can then use the count() method to count the number of
    # zeros, and return the difference between the number of ones and the
    # number of zeros.  This will be negative if the number of ones is
    # greater than the number of zeros, positive if the number of ones is
    # less than the number of zeros, and zero if the number of ones and
    # the number of zeros are the same.
    #
    # We can use the built-in function cmp_to_key() to convert the custom
    # sort function into a custom key function.
    #
    # Finally, we can use the list.sort() method with the key parameter to
    # sort the array using the custom key function.
    arr.sort(key=cmp_to_key(lambda a, b: -1 if bin(a).count("1") - bin(b).count("1") else 1 if bin(a).count("1") - bin(b).count("1") < 0 else 0))
    return arr
    
def