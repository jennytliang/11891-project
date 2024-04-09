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

    def juxtapose_nums(arr):
        return [int(x) for x in str(arr)]

    def sum_nums(arr):
        return sum(arr)

    def count_positive_nums(arr):
        count = 0
        for num in arr:
            if num > 0:
                count += 1
        return count

    def count_nums(arr):
        return count_positive_nums(juxtapose_nums(arr))

    return count_nums(arr)


print(count_nums([1, 2, 3]))  # = 3
print(count_nums([-1, 11, -11]))  # = 1
print(count_nums([0]))  # = 0
print(count_nums([-1, -2, -3]))  # = 0
print(count_nums([-123, 123, 120]))  # = 2
print(count_nums([-321, -320, 321]))  # = 1
