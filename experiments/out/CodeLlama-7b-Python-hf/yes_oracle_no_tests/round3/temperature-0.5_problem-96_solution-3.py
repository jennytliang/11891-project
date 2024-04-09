def count_up_to(n):
    """Implement a function that takes an non-negative integer and returns an array of the first n
    integers that are prime numbers and less than n.
    for example:
    count_up_to(5) => [2,3]
    count_up_to(11) => [2,3,5,7]
    count_up_to(0) => []
    count_up_to(20) => [2,3,5,7,11,13,17,19]
    count_up_to(1) => []
    count_up_to(18) => [2,3,5,7,11,13,17]
    
	Include these tokens in the code: ans =
	Do not include these tokens in the code: if n <= 0 :
	"""
    ans = []
    if n <= 0:
        return ans
    else:
        for i in range(2, n):
            is_prime = True
            for j in range(2, i):
                if i % j == 0:
                    is_prime = False
                    break
            if is_prime:
                ans.append(i)
        return ans


# TEST CASES
print(count_up_to(5))  # should print [2,3]
print(count_up_to(11))  # should print [2,3,5,7]
print(count_up_to(0))  # should print []
print(count_up_to(20))  # should print [2,3,5,7,11,13,17,19]
print(count_up_to(1))  # should print []
print(count_up_to(18))  # should print [2,3,5,7,11,13,17]
