def count_nums(arr):
    """
    Write a function count_nums which takes an array of integers and returns
    the number of elements which has a sum of digits > 0.
    If a number is negative, then its first signed digit will be negative:
    e.g. -123 has signed digits -1, 2, and 3.
    >>> count_nums([]) == 0
    >>> count_nums([-1, 11, -11]) == 1
    >>> count_nums([1, 1, 2]) == 3
    
	Include these tokens in the code: def judge
	Do not include these tokens in the code: if len
	"""
    def judge(num):
        num = str(num)
        if num[0] == '-':
            num = num[1:]
        return sum([int(i) for i in list(num)]) > 0
    return sum([judge(i) for i in arr])
    
def count_nums(arr):
    """
    Write a function count_nums which takes an array of integers and returns
    the number of elements which has a sum of digits > 0.
    If a number is negative, then its first signed digit will be negative:
    e.g. -123 has signed digits -1, 2, and 3.
    >>> count_nums([]) == 0
    >>> count_nums([-1, 11, -11]) == 1
    >>> count_nums([1, 1, 2]) == 3
    
	Include these tokens in the code: def judge
	Do not include these tokens in the code: if len
	"""
    def judge(num):
        num = str(num)
        if num[0] == '-':
            num = num[1:]
        return sum([int(i) for i in list(num)]) > 0
    return sum([judge(i) for i in arr])
    
    
if __name__ == '__main__':
    import doctest
    doctest.testmod()
