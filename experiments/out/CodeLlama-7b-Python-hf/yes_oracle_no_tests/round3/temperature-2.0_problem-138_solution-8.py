def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    
	Include these tokens in the code: return n >=
	"""
    if n >= 8:
        return True
    else:
        return False


def main():
    print(is_equal_to_sum_even(4))
    print(is_equal_to_sum_even(6))
    print(is_equal_to_sum_even(8))
    print(is_equal_to_sum_even(9))
    print(is_equal_to_sum_even(10))
    print(is_equal_to_sum_even(12))
    print(is_equal_to_sum_even(14))
    print(is_equal_to_sum_even(16))


if __name__ == "__main__":
    main()
