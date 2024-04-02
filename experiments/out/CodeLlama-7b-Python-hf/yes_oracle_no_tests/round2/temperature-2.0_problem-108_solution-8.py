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


    def j(arr):
        l = []
        for i in arr:
            if i >= 0:
                l.append(i)
            else:
                l.append(-i)
        return l

    def k(arr):
        l = []
        for i in arr:
            if i <= 0:
                l.append(i)
            else:
                l.append(-i)
        return l

    def count_nums(arr):
        return len(j(arr)) + len(k(arr))

    return count_nums(arr)



print(count_nums([1, 1, 2]))
print(count_nums([-1, 11, -11]))
print(count_nums([]))
