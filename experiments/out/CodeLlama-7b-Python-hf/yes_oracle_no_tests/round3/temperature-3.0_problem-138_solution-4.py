def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    
	Include these tokens in the code: >=
	Do not include these tokens in the code: %
	"""


    re = []
    for i in range(1,n+1):
        if i%2 == 0:
            re.append(i)
    for i in range(len(re)):
        for j in range(len(re)-i):
            for k in range(len(re)-j-1):
                if re[i] + re[j] + re[j+1] + re[k] == n:
                    return True
    return False






































































































































































































































































































































































































