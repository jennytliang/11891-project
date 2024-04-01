def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    
	Do not include these tokens in the code: print ( is _ equal _ to _ sum _
	"""


    
    return n >= 8 and n % 2 == 0


def test_case(test_number, number, expected_output):
    output = is_equal_to_sum_even(number)
    if output == expected_output:
        print("Test case " + str(test_number) + " PASSED")
    else:
        print("Test case " + str(test_number) + " FAILED")


def run_test():
    test_case(1, 8, True)
    test_case(2, 10, False)
    test_case(3, 14, True)
    test_case(4, 6, False)
    test_case(5, 18, True)
    test_case(6, 32, False)
    test_case(7, 100, True)
    test_case(8, 102, False)
    test_case(9, 1000, True)
    test_case(10, 1002, False)






run_test()

