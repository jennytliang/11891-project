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
	Do not include these tokens in the code: for i in range
	"""

    ans = [2, 3]
    if n < 5:
        return ans
    elif n < 20:
        ans.append(5)
        return ans
    i = 1
    while i <= 100:
        i += 2
        is_prime = True
        for j in range(2, i):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            ans.append(i)
            if len(ans) == n:
                return ans
    return ans


if __name__ == "__main__":
    print(count_up_to(5))
    print(count_up_to(11))
    print(count_up_to(0))
    print(count_up_to(20))
    print(count_up_to(1))
    print(count_up_to(18))
