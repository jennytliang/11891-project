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
    numbers = []
    for i in range(n):
        numbers.append(i)
    
    for number in numbers:
        is_prime = True
        for i in range(2, number, 1):
            if number % i == 0:
                is_prime = False
        
        if is_prime:
            ans.append(number)
    
    return ans

# tests
assert count_up_to(0) == [], 'Count up to 0 does not return []'
assert count_up_to(1) == [], 'Count up to 1 does not return []'
assert count_up_to(5) == [2,3], 'Count up to 5 does not return [2,3]'
assert count_up_to(11) == [2,3,5,7], 'Count up to 11 does not return [2,3,5,7]'
assert count_up_to(20) == [2,3,5,7,11,13,17,19], 'Count up to 20 does not return []'