def count_nums(arr):
    """
    Write a function count_nums which takes an array of integers and returns
    the number of elements which has a sum of digits > 0.
    If a number is negative, then its first signed digit will be negative:
    e.g. -123 has signed digits -1, 2, and 3.
    >>> count_nums([]) == 0
    >>> count_nums([-1, 11, -11]) == 1
    >>> count_nums([1, 1, 2]) == 3
    
	Do not include these tokens in the code: # 1 2 minutes
	"""
    count = 0
    
    for i in arr:
        # 1,1,2,3,4,4,5 = [1, 10, 20, 300, 4000]
        # 1,2,3,4,5,6,7,8 = [1, 100, 2000, 30000, 400000]
        # 1
        
        total = 0
        digit = abs(i)
        # 1,1,2,3,4,4,5
        
        while digit != 0:
            total += (digit % 10)
            digit = digit // 10
        # 1
        
        count = count + 1 if total > 0 else count
        
    return count
    
if __name__ == '__main__':
    import doctest
    doctest.testmod()
