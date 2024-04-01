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
    
	Include these tokens in the code:  ans
	Do not include these tokens in the code: pr imes
	"""

    ans = []
    if n <= 1:
        return ans

    i = 2

    while i < n:
        if is_prime(i):
            ans.append(i)
        i += 1

    return ans


def is_prime(n):
    i = 2

    while i * i <= n:
        if n % i == 0:
            return False
        i += 1

    return True
