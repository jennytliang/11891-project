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

    def juxtapose(a, b):
        """
        Write a function juxtapose which takes two integers and returns a list
        with the two integers side-by-side.
        >>> juxtapose(1, 2)
        [1, 2]
        >>> juxtapose(-1, 2)
        [-1, 2]
        """
        return [a, b]

    def sum_digits(arr):
        """
        Write a function sum_digits which takes a list of integers and returns
        the sum of the digits in each integer.
        >>> sum_digits([]) == 0
        >>> sum_digits([1, 12, 123]) == 4
        """
        return sum(map(sum, map(digits, arr)))

    def digits(num):
        """
        Write a function digits which takes an integer and returns a list of
        the signed digits in the integer.
        >>> digits(123)
        [1, 2, 3]
        >>> digits(-123)
        [-1, 2, 3]
        >>> digits(0)
        [0]
        """
        return list(map(int, str(num)))

    l = []
    for i in range(len(arr)):
        if sum_digits(digits(arr[i])) > 0:
            l.append(arr[i])
    return len(l)


def count_nums(arr):
    return len([x for x in arr if sum(digits(x)) > 0])


def digits(num):
    return [int(x) for x in str(num)]


def sum_digits(arr):
    return sum(map(sum, map(digits, arr)))


def juxtapose(a, b):
    return [a, b]


if __name__ == "__main__":
    import doctest

    doctest.testmod()
