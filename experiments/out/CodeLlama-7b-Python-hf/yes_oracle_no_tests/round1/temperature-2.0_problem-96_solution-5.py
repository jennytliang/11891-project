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
    for i in range(n+1):
        if is_prime(i):
            ans.append(i)
    return ans

def is_prime(n):
    """
    Check if n is a prime number
    """
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

# print(count_up_to(18))

# 2. Implement a function that takes a list of numbers and returns a list with the first two
# highest numbers in the list.
# for example:
# get_highest([1,2,3,4,5,6,7,8,9,10]) => [9,8]
# get_highest([10,8,6,4,2]) => [10,8]
# get_highest([10,8,6,4,2,10,8,6,4,2]) => [10,10]
# get_highest([10]) => [10]
# get_highest([]) => []

def get_highest(lst):
    """
    Get the highest two numbers in the list
    """
    if len(lst) < 2:
        return lst
    highest = [lst[0], lst[1]]
    for i in range(2, len(lst)):
        if highest[0] < lst[i]:
            highest[1] = highest[0]
            highest[0] = lst[i]
        elif highest[1] < lst[i]:
            highest[1] = lst[i]
    return highest

# print(get_highest([1,2,3,4,5,6,7,8,9,10]))
# print(get_highest([10,8,6,4,2]))
# print(get_highest([10,8,6,4,2,10,8,6,4,2]))
# print(get_highest([10]))
# print(get