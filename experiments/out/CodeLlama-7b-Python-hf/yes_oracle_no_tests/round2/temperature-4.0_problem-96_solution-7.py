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
    
	Do not include these tokens in the code: pass # Test ing
	"""
    # write your code here
    prime_numbers = []
    for i in range(n):
        if i == 0:
            i += 1
        if i == 1:
            continue
        if i > 1:
            for j in range(2, i):
                if i % j == 0:
                    break
            else:
                prime_numbers.append(i)
    return prime_numbers


print(count_up_to(5))
print(count_up_to(11))
print(count_up_to(0))
print(count_up_to(20))
print(count_up_to(1))
print(count_up_to(18))
