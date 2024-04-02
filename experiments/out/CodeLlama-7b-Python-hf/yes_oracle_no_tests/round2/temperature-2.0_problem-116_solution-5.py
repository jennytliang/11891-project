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
    # The idea is to sort the list based on the number of ones in the binary representation
    # of each number.
    # We can do this by creating a dictionary of number of ones in binary representation
    # to a list of numbers with that many ones.
    # Then we can sort the dictionary by the number of ones in the binary representation
    # and then flatten the dictionary to a list.
    # Finally we sort the list of numbers by their decimal value.

    # Create a dictionary of number of ones in binary representation to a list of numbers
    # with that many ones.
    ones = {}
    for num in arr:
        # Get the number of ones in the binary representation of the number
        ones_count = bin(num).count("1")
        # Add the number to a list of numbers with that many ones
        if ones_count not in ones:
            ones[ones_count] = [num]
        else:
            ones[ones_count].append(num)

    # Sort the dictionary by the number of ones in the binary representation
    ones = {k: v for k, v in sorted(ones.items())}
    # Flatten the dictionary to a list
    ones = [item for sublist in ones.values() for item in sublist]
    # Sort the list of numbers by their decimal value
    ones = sorted(ones)

    return ones


# Some console.log tests
print(sort_array([1, 5, 2, 3, 4]))  # [1, 2, 3, 4, 5]
print(sort_array([-2, -3, -4, -5, -6]))  # [-6, -5, -4, -3, -2]
print(sort_array([1, 0, 2, 3, 4]))  # [0, 1, 2, 3, 4]
print(sort_array([4, 1, 2, 3]))  # [1, 2, 3, 4]
print(sort_array([3, 2, 4, 1]))  # [1, 2, 3,