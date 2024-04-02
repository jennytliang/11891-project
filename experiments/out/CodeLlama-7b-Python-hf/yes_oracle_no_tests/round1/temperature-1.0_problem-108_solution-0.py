def count_nums(arr):
    """
    Write a function count_nums which takes an array of integers and returns
    the number of elements which has a sum of digits > 0.
    If a number is negative, then its first signed digit will be negative:
    e.g. -123 has signed digits -1, 2, and 3.
    >>> count_nums([]) == 0
    >>> count_nums([-1, 11, -11]) == 1
    >>> count_nums([1, 1, 2]) == 3
    
	Include these tokens in the code: def judge ( x : int ) -> int :
	"""
    def judge(x):
        """
        Returns 1 if the sum of digits of x is positive, else returns 0.
        """
        if x < 0:
            return judge(-x)
        if x < 10:
            return 1 if x > 0 else 0
        return judge(x // 10) + judge(x % 10)
    return sum(judge(x) for x in arr)


if __name__ == '__main__':
    import doctest
    doctest.testmod()
