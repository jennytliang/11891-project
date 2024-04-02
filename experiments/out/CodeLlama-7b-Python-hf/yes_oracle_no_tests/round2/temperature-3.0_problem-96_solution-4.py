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
    
	Include these tokens in the code: is prime = [ True ] * ( n +
	Do not include these tokens in the code: if <=
	"""

    ans = [2, 3]
    i = 5
    while len(ans) < n and i < n:
        is_prime = True
        for j in ans:
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            ans.append(i)
        i += 2
    return ans


def count_up_to_v2(n):
    """Implement a function that takes an non-negative integer and returns an array of the first n
    integers that are prime numbers and less than n.
    for example:
    count_up_to_v2(5) => [2,3]
    count_up_to_v2(11) => [2,3,5,7]
    count_up_to_v2(0) => []
    count_up_to_v2(20) => [2,3,5,7,11,13,17,19]
    count_up_to_v2(1) => []
    count_up_to_v2(18) => [2,3,5,7,11,13,17]
    
	Include these tokens in the code: is prime = [ True ] * ( n +
	Do not include these tokens in the code: if <=
	"""

    ans = [2, 3]
    i = 5
    while len(ans) < n and i < n:
        is_prime = True
        for j in ans:
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            ans.append(i)
            i += 2
        else:
            i += 2
    return ans
