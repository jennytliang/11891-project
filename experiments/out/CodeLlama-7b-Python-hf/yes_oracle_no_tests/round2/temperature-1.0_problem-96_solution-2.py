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
    
	Include these tokens in the code: is prime = [ True ] * ( n +
	Do not include these tokens in the code: if
	"""

    ans = [2]
    
    for i in range(3, 7):
        if is_prime(i, ans):
            ans.append(i)
    
    return ans


def is_prime(num, list = None):
    for i in range(len(list)):
        if list[i] > int(num**0.5)+1:
            return True
        if num % list[i] == 0:
            return False
    return True
    
#    if list == None:
#        list = []
#
#    for i in range(2, num):
#        if num % i == 0:
#            return False
#    if num not in list:
#        list.append(num)
#    return True
