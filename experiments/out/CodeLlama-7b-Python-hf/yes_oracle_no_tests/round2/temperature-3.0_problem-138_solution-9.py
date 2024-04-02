def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    
	Do not include these tokens in the code: # TODO : Write a solution here
	"""
    # Write your code below this line
    sum = 0
    for i in range(1, n + 1):
        if i % 2 == 0:
            sum += i
    if sum == n:
        return True
    else:
        return False
    # Write your code above this line


# Do not edit the function call
print(is_equal_to_sum_even(4))
print(is_equal_to_sum_even(6))
print(is_equal_to_sum_even(8))
print(is_equal_to_sum_even(10))
