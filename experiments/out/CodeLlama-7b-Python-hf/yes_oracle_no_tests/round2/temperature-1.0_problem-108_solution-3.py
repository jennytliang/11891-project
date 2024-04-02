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

    def ju(num):
        return num < 0

    def sh(num):
        return num // 10

    def mod(num):
        return num % 10

    def sum_(num):
        if num < 10:
            return num
        else:
            return num % 10 + sum_(sh(num))

    def count(arr):
        count = 0
        for num in arr:
            if sum_(abs(num)) > 0:
                count += 1
        return count

    return count(arr)


print(count_nums([-1, 11, -11]))
