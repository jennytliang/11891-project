def count_nums(arr):
    """
    Write a function count_nums which takes an array of integers and returns
    the number of elements which has a sum of digits > 0.
    If a number is negative, then its first signed digit will be negative:
    e.g. -123 has signed digits -1, 2, and 3.
    >>> count_nums([]) == 0
    >>> count_nums([-1, 11, -11]) == 1
    >>> count_nums([1, 1, 2]) == 3
    
	Include these tokens in the code: def judge ( x : int ) -> int :
	"""

    # 12 minutes

    digits = {'0', '1', '2', '3', '4', '5', '6', '7',
              '8', '9', '-', '+'}

    def first_signed_digit(n):
        """
        Returns n's first number's sign.
        """
        return n / abs(n)

    def sum_digits(n):
        s = 0
        while n > 0:
            s += n % 10
            n = n // 10
        return s

    # return sum(1 for n in arr if first_signed_digit(n) * sum_digits(n) > 0)

    counter = 0
    for n in arr:
        if first_signed_digit(n) * sum_digits(n) > 0:
            counter += 1
    return counter


count_nums([10011, -11])
# print(count_nums([13464, 8464, -15614, 84644]))
