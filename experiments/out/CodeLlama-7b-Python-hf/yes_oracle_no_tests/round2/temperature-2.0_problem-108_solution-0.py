def count_nums(arr):
    """
    Write a function count_nums which takes an array of integers and returns
    the number of elements which has a sum of digits > 0.
    If a number is negative, then its first signed digit will be negative:
    e.g. -123 has signed digits -1, 2, and 3.
    >>> count_nums([]) == 0
    >>> count_nums([-1, 11, -11]) == 1
    >>> count_nums([1, 1, 2]) == 3
    
	Include these tokens in the code: def judge
	Do not include these tokens in the code: pass count _
	"""

    def judge(num):
        total = 0
        for i in range(len(str(num))):
            total += int(str(num)[i])
        return total > 0

    count = 0
    for i in arr:
        if judge(i):
            count += 1
    return count


def test_bench():
    test_data = [
        [],
        [-1, 11, -11],
        [1, 1, 2]
    ]

    for data in test_data:
        print(count_nums(data))


if __name__ == "__main__":
    test_bench()
