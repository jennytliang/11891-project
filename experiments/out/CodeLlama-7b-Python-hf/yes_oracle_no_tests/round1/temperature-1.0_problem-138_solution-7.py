def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    
	Include these tokens in the code: return n >=
	"""
    if n >= 4:
        a = n
        while a > 0:
            rest = a % 4
            a = a - rest
            if a == 0:
                return True
            a -= 1
    return False


def test_function(test_case):
    n = test_case[0]
    solution = test_case[1]
    output = is_equal_to_sum_even(n)
    if output == solution:
        print("Pass")
    else:
        print("Fail")

test_function([6,False])
test_function([8,True])
test_function([10,False]) 