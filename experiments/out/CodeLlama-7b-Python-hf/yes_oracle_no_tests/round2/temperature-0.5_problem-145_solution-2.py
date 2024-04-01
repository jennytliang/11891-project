def order_by_points(nums):
    """
    Write a function which sorts the given list of integers
    in ascending order according to the sum of their digits.
    Note: if there are several items with similar sum of their digits,
    order them based on their index in original list.

    For example:
    >>> order_by_points([1, 11, -1, -11, -12]) == [-1, -11, 1, -12, 11]
    >>> order_by_points([]) == []
    
	Do not include these tokens in the code: # My solution #
	"""
    
    def sum_of_digits(n):
        return sum(map(int, str(n)))
    
    def is_even(n):
        return n % 2 == 0
    
    def is_odd(n):
        return not is_even(n)
    
    def is_greater(n1, n2):
        return n1 > n2
    
    def is_less(n1, n2):
        return n1 < n2
    
    def is_equal(n1, n2):
        return n1 == n2
    
    def is_prime(n):
        if n % 2 == 0 and n > 2:
            return False
        return all(n % i for i in range(3, int(n ** 0.5) + 1, 2))
    
    def is_palindrome(n):
        return str(n) == str(n)[::-1]
    
    def is_multiple_of_3(n):
        return n % 3 == 0
    
    def is_multiple_of_5(n):
        return n % 5 == 0
    
    def is_multiple_of_7(n):
        return n % 7 == 0
    
    def is_multiple_of_13(n):
        return n % 13 == 0
    
    def is_multiple_of_2(n):
        return n % 2 == 0
    
    def is_multiple_of_35(n):
        return n % 35 == 0
    
    def is_multiple_of_49(n):
        return n % 49 == 0
    
    def is_multiple_of_6(n):
        return n % 6 == 0
    
    def is_multiple_of_8(n):
        return n % 8 == 0
    
    def is_multiple_of_9(n):
        return n % 9 == 0
    
    def is_multiple_of_10(n