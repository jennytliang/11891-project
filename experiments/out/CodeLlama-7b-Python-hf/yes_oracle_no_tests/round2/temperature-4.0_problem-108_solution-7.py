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

    def ju(s):
        if s < 0:
            return s
        if s == 0:
            return 0
        return s % 10 + ju(s // 10)

    def count_nums(arr):
        if arr == []:
            return 0
        return 1 + count_nums([x for x in arr if ju(x) > 0])

    return count_nums(arr)


print(count_nums([-1, 11, -11]))
