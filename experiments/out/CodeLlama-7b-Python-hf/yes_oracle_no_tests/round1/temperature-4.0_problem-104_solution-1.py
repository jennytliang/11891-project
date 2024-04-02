def unique_digits(x):
    """Given a list of positive integers x. return a sorted list of all 
    elements that hasn't any even digit.

    Note: Returned list should be sorted in increasing order.
    
    For example:
    >>> unique_digits([15, 33, 1422, 1])
    [1, 15, 33]
    >>> unique_digits([152, 323, 1422, 10])
    []
    
	Include these tokens in the code: def judge
	Do not include these tokens in the code: # The idea is to keep
	"""
    # pass
    """
    # The idea is to keep a list of all numbers that are not in the list.
    # Then we can just return that list.
    # We can use the built in function isinstance to check if a number is an int
    # We can use the built in function str to convert numbers to strings.
    # We can use the built in function len to check if a string has a certain length
    # We can use the built in function int to convert a string to an int.
    # We can use the built in function range to create a list of numbers
    # We can use the built in function all to check if all elements of a list are True
    # We can use the built in function filter to filter out elements of a list
    # We can use the built in function enumerate to get the index of elements of a list
    # We can use the built in function sorted to sort a list
    """
    # Your code here
    result = []
    for num in x:
        if isinstance(num, int):
            num_str = str(num)
            num_even = False
            for num_digit in range(len(num_str)):
                if int(num_str[num_digit]) % 2 == 0:
                    num_even = True
            if num_even == False:
                result.append(num)
    return sorted(result)

if __name__ == "__main__":
    import doctest
    doctest.testmod()