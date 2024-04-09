def count_nums(arr):
    """
    Write a function count_nums which takes an array of integers and returns
    the number of elements which has a sum of digits > 0.
    If a number is negative, then its first signed digit will be negative:
    e.g. -123 has signed digits -1, 2, and 3.
    >>> count_nums([]) == 0
    >>> count_nums([-1, 11, -11]) == 1
    >>> count_nums([1, 1, 2]) == 3
    
	Include these tokens in the code: x : int ) -> int :
	Do not include these tokens in the code: num ):
	"""

    def j(x):
        if x < 0:
            return x
        else:
            return x * -1

    def k(y):
        if y < 0:
            return y
        else:
            return y * -1

    def count_nums(arr):
        num = 0
        for i in arr:
            x = j(i)
            if x < 0:
                x = k(i)
            y = str(x)
            z = 0
            for j in y:
                z += int(j)
            if z > 0:
                num += 1
        return num

    return count_nums(arr)


print(count_nums([1, 1, 2]))
