def count_nums(arr):
    """
    Write a function count_nums which takes an array of integers and returns
    the number of elements which has a sum of digits > 0.
    If a number is negative, then its first signed digit will be negative:
    e.g. -123 has signed digits -1, 2, and 3.
    >>> count_nums([]) == 0
    >>> count_nums([-1, 11, -11]) == 1
    >>> count_nums([1, 1, 2]) == 3
    
	Include these tokens in the code: ( x :
	"""

    def  count_nums(arr):
        count = 0
        for num in arr:
            if sum(int(digit) for digit in str(num)) > 0:
                count += 1
        return count

    return count_nums(arr)


# print(count_nums([-1, 11, -11]))
# print(count_nums([1, 1, 2]))
# print(count_nums([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
# print(count_nums([0, 0, 0, 0, 0, 0, 0, 0, 0, 0]))
# print(count_nums([-1, -2, -3, -4, -5, -6, -7, -8, -9, -10]))
# print(count_nums([-1, -11, -11]))
# print(count_nums([1, 11, 11]))
# print(count_nums([1, 11, 21]))
# print(count_nums([1, 11, 22]))
# print(count_nums([1, 11, 23]))
# print(count_nums([1, 11, 24]))
# print(count_nums([1, 11, 25]))
# print(count_nums([1, 11, 26]))
# print(count_nums([1, 11, 27]))
# print(count_nums([1, 11, 28]))
# print(count_nums([1, 11, 29]))
# print(count_nums([1, 11, 30]))
# print(count_nums([1, 11, 31]))
# print(count_nums([1, 11, 32]))
# print(count_nums([1, 11, 