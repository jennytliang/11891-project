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
    # prime_numbers = [2,3,5,7]
    # ans = []
    # for num in prime_numbers:
    #     if num < n:
    #         ans.append(num)
    # return ans

    # ans = []
    # for i in range(2,n):
    #     is_prime = True
    #     for j in range(2, i):
    #         if i % j == 0:
    #             is_prime = False
    #             break
    #     if is_prime:
    #         ans.append(i)
    # return ans

    ans = []
    for i in range(2, n):
        is_prime = True
        for j in range(2, i):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            ans.append(i)
    return ans


if __name__ == "__main__":
    print(count_up_to(10))
    print(count_up_to(18))
    print(count_up_to(20))
    print(count_up_to(0))
