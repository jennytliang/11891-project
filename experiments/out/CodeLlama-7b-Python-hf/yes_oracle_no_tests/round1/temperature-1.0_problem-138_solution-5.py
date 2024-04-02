def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    
	Include these tokens in the code: return n >=
	"""
    return n // 2 >= 4


def main():
    print("Do the following assertions hold?")
    print("(10 should be False)")
    assert not is_equal_to_sum_even(10)
    print("(8 should be True)")
    assert is_equal_to_sum_even(8)
    print("(12345 should be False)")
    assert not is_equal_to_sum_even(12345)


if __name__ == "__main__":
    main()
