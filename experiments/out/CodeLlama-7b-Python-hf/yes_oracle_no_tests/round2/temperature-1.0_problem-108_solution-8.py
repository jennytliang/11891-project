def count_nums(arr):
    """
    Write a function count_nums which takes an array of integers and returns
    the number of elements which has a sum of digits > 0.
    If a number is negative, then its first signed digit will be negative:
    e.g. -123 has signed digits -1, 2, and 3.
    >>> count_nums([]) == 0
    >>> count_nums([-1, 11, -11]) == 1
    >>> count_nums([1, 1, 2]) == 3
    
	Include these tokens in the code: : int ) -> int :
	Do not include these tokens in the code: ):
	"""


    def jj(arr):
        for i in arr:
            j= sum(map(lambda x: ord(x)-48, str(abs(i))))
            if j>0:
                yield 1


    return len(list(jj(arr)))
print(count_nums([-1, -3, 8, 42, 144]))


# RW 27/05/2021
# Difference between 'def' and 'def f(x):'
"""
The former defines a function "jj" where as the latter is the 
use of a function "jj" to solve another problem
"""


