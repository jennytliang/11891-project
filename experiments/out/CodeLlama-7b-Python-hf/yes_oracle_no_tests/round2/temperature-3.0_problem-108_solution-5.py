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

    def juxtapose(arr):
        return [int(i) for i in str(sum(arr))]

    def count_nums(arr):
        return len([i for i in arr if sum(juxtapose(i)) > 0])


def test_bench():
    test_data = [
        [],
        [-1, 11, -11],
        [1, 1, 2],
    ]

    for i in test_data:
        print(count_nums(i))


if __name__ == "__main__":
    test_bench()
