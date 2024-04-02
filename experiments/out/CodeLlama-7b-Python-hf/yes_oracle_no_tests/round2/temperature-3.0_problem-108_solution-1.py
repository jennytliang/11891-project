def count_nums(arr):
    """
    Write a function count_nums which takes an array of integers and returns
    the number of elements which has a sum of digits > 0.
    If a number is negative, then its first signed digit will be negative:
    e.g. -123 has signed digits -1, 2, and 3.
    >>> count_nums([]) == 0
    >>> count_nums([-1, 11, -11]) == 1
    >>> count_nums([1, 1, 2]) == 3
    
	Include these tokens in the code: : int ) -> int : l =
	Do not include these tokens in the code: ):
	"""

    def ju(num):
        if num < 0:
            return -num
        else:
            return num

    def sum_digits(num):
        return sum([int(x) for x in str(num)])

    l = len(arr)
    count = 0
    for i in range(l):
        if sum_digits(ju(arr[i])) > 0:
            count += 1
    return count


print(count_nums([1, 1, 2]))
