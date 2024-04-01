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


    def josephus(arr, k):
        """
        Josephus Problem:
        There are n people standing in a circle. They are numbered from 1 to n.
        Starting from the person with the number 1, each person kicks the person
        standing next to him. The person who is kicked dies. The person who
        kicks him becomes 1. This process continues until the person with the
        number n dies. The process stops when only one person is left standing.
        Find out who will be the last person standing.
        """
        if len(arr) == 0:
            return 0
        if len(arr) == 1:
            return arr[0]
        elif len(arr) == 2:
            return arr[0] if arr[0] != arr[1] else arr[1]
        elif len(arr) > 2:
            return josephus([i for i in arr[1::2] if i != arr[0]], k)

    def count_nums(arr):
        """
        Write a function count_nums which takes an array of integers and returns
        the number of elements which has a sum of digits > 0.
        If a number is negative, then its first signed digit will be negative:
        e.g. -123 has signed digits -1, 2, and 3.
        """
        return len(
            [i for i in arr if josephus([int(i) for i in str(i)], 1) > 0]
        )

    return count_nums(arr)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
