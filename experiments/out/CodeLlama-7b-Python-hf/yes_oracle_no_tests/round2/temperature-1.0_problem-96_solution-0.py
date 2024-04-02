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
    
	Include these tokens in the code: ans = [] is prime = [ True
	"""
    if n < 0:
        return [] # 0 is not prime
    prime = [True] * (n + 1)
    prime[0] = False
    for key in range(2,int((n-1) ** 0.5)+1):
        for value in range(2 * key, n+1, key):
            prime[value] = False
    return [key for key in range(n+1) if prime[key] == True]

ans = count_up_to(10)
print (ans)