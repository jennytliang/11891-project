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
    
	Include these tokens in the code: ans
	Do not include these tokens in the code: prime _ numbers
	"""
    ans = []
    for i in range(2, n + 1):
        if is_prime(i):
            ans.append(i)
    return ans


def is_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def count_up_to2(n):
    ans = []
    for i in range(2, n + 1):
        if is_prime2(i):
            ans.append(i)
    return ans


def is_prime2(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def count_up_to3(n):
    ans = []
    for i in range(2, n + 1):
        if is_prime3(i):
            ans.append(i)
    return ans


def is_prime3(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def count_up_to4(n):
    ans = []
    for i in range(2, n + 1):
        if is_prime4(i):
            ans.append(i)
    return ans


def is_prime4(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def count_up_to5(n):
    ans = []
    for i in range(2, n + 1):
        if is_prime5(i):
            ans.append(i)
    return ans


def is_prime5(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def count_up_to6(n):
    ans = []
    for i in range(2, n + 1):
        if is_prime6(i):
            ans.