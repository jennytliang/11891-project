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

    def ju(a):
        if a < 0:
            return -a
        else:
            return a

    def sum_nums(a):
        summ = 0
        for i in range(len(a)):
            summ += ju(a[i])
        return summ

    def count_nums(a):
        summ = 0
        for i in range(len(a)):
            if sum_nums(a[i]) > 0:
                summ += 1
        return summ

    return count_nums(arr)


print(count_nums([1, 2, 3, 4, 5, -1, -2, -3, -4, -5]))
