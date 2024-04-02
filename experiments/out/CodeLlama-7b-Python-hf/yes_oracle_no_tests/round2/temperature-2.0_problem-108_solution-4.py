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

    def ju(arr):
        l = []
        for i in arr:
            l.append(i)
        return l

    def f(arr):
        l = ju(arr)
        for i in l:
            if i < 0:
                l.remove(i)
        return l

    def g(arr):
        l = ju(arr)
        for i in l:
            if i > 0:
                l.remove(i)
        return l

    def h(arr):
        l = ju(arr)
        for i in l:
            if i == 0:
                l.remove(i)
        return l

    def k(arr):
        l = ju(arr)
        for i in l:
            if i < 0:
                l.remove(i)
        return l

    def j(arr):
        l = ju(arr)
        for i in l:
            if i > 0:
                l.remove(i)
        return l

    def i(arr):
        l = ju(arr)
        for i in l:
            if i == 0:
                l.remove(i)
        return l

    def count_nums(arr):
        l = ju(arr)
        return len(l)

    return count_nums(arr)
