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
        l = len(arr)
        for i in range(l):
            if arr[i] < 0:
                arr[i] *= -1
        return arr

    def g(arr):
        l = len(arr)
        for i in range(l):
            num = str(arr[i])
            k = len(num)
            for i in range(k):
                arr[i] += int(num[i])
        return arr

    def h(arr):
        l = len(arr)
        for i in range(l):
            if arr[i] > 0:
                return 1

    def count_nums(arr):
        return h(g(j(arr)))


if __name__ == "__main__":
    import doctest
    doctest.testmod()