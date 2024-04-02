def count_nums(arr):
    """
    Write a function count_nums which takes an array of integers and returns
    the number of elements which has a sum of digits > 0.
    If a number is negative, then its first signed digit will be negative:
    e.g. -123 has signed digits -1, 2, and 3.
    >>> count_nums([]) == 0
    >>> count_nums([-1, 11, -11]) == 1
    >>> count_nums([1, 1, 2]) == 3
    
	Include these tokens in the code: ( x :
	"""

    def 
    """
    This code is wrong and it is not passing all the tests, but I got an idea
    from it: what about splitting negative numbers into their parts
    and adding those parts as well?
    """
    def count_nums_fast(arr):
        from functools import reduce

        def split_sign(x):
            return ("-", "-")[int(x < 0)] + str(abs(x))
        
        return sum( map(lambda x: x > 0,
                        map(lambda x: sum( map(int,
                                                split_sign(x).split("-"))),
                            arr))
        )
