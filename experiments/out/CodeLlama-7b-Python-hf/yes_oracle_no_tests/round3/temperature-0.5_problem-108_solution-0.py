def count_nums(arr):
    """
    Write a function count_nums which takes an array of integers and returns
    the number of elements which has a sum of digits > 0.
    If a number is negative, then its first signed digit will be negative:
    e.g. -123 has signed digits -1, 2, and 3.
    >>> count_nums([]) == 0
    >>> count_nums([-1, 11, -11]) == 1
    >>> count_nums([1, 1, 2]) == 3
    
	Include these tokens in the code: judge
	Do not include these tokens in the code: j
	"""



    # =============================================================================
    # # Solution 1
    # def sum_digits(n):
    #     total = 0
    #     while n > 0:
    #         total += n % 10
    #         n = n // 10
    #     return total
    # 
    # def count_nums(arr):
    #     return sum([sum_digits(i) > 0 for i in arr])
    # =============================================================================



    # =============================================================================
    # # Solution 2
    # def sum_digits(n):
    #     total = 0
    #     while n > 0:
    #         total += n % 10
    #         n = n // 10
    #     return total
    # 
    # def count_nums(arr):
    #     return sum([sum_digits(abs(i)) > 0 for i in arr])
    # =============================================================================



    # =============================================================================
    # # Solution 3
    # def sum_digits(n):
    #     total = 0
    #     while n > 0:
    #         total += n % 10
    #         n = n // 10
    #     return total
    # 
    # def count_nums(arr):
    #     return sum([sum_digits(abs(i)) > 0 for i in arr])
    # =============================================================================



    # =============================================================================
    # # Solution 4
    # def count_nums(arr):
    #     return sum([sum(map(int, str(abs(i)))) > 0 for i in arr])
    # =============================================================================



    # =============================================================================
    # # Solution 5
    # def count_nums(arr):
    #     return sum([sum(map(int, str(abs(i))[1:])) > 0 for i in