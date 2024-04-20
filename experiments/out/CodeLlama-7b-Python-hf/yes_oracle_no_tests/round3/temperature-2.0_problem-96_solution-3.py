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
    
	Include these tokens in the code: ans = []
	"""
    ans = []
    for i in range(2, n+1):
        isPrime = True
        for j in range(2, i):
            if i % j == 0:
                isPrime = False
                break
        if isPrime:
            ans.append(i)
    return ans


# print(count_up_to(5))
# print(count_up_to(11))
# print(count_up_to(0))
# print(count_up_to(20))
# print(count_up_to(1))
# print(count_up_to(18))


def count_up_to_no_while(n):
    """Implement a function that takes an non-negative integer and returns an array of the first n
    integers that are prime numbers and less than n.
    for example:
    count_up_to(5) => [2,3]
    count_up_to(11) => [2,3,5,7]
    count_up_to(0) => []
    count_up_to(20) => [2,3,5,7,11,13,17,19]
    count_up_to(1) => []
    count_up_to(18) => [2,3,5,7,11,13,17]
    
	Include these tokens in the code: ans = []
	"""
    ans = []
    for i in range(2, n+1):
        if all(i % j != 0 for j in range(2, i)):
            ans.append(i)
    return ans


# print(count_up_to_no_while(5))
# print(count_up_to_no_while(11))
# print(count_up_to_no_while(0))
# print(count_up_to_no_while(20))
# print(count_up_to_no_while(1))
# print(count_up_to_no_while(18))