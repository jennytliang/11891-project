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
    
	Include these tokens in the code: is prime = [ True ] * (
	"""

    ans = []
    for i in range(2, n):
        if is_prime(i):
            ans.append(i)
    return ans


def is_prime(n):
    """Helper function that returns true if n is prime."""
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


print(is_prime(10))
