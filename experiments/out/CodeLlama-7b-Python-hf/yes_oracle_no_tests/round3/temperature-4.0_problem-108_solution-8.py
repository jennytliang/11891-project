def count_nums(arr):
    """
    Write a function count_nums which takes an array of integers and returns
    the number of elements which has a sum of digits > 0.
    If a number is negative, then its first signed digit will be negative:
    e.g. -123 has signed digits -1, 2, and 3.
    >>> count_nums([]) == 0
    >>> count_nums([-1, 11, -11]) == 1
    >>> count_nums([1, 1, 2]) == 3
    
	Do not include these tokens in the code: # your code here
	"""
    # your code here
    def sum_digits(number):
        result = 0
        while number > 0:
            result += number % 10
            number //= 10
        return result

    return sum(sum_digits(num) > 0 for num in arr)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
