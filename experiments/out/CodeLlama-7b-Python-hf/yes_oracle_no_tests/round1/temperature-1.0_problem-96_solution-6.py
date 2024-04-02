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
    import math
    def is_prime(target_number):
        factor = 2
        for i in range(2, int(math.sqrt(target_number)) + 1):
            if target_number % i == 0:
                return False
        return True
    ans = []

    for i in range(2,n + 1):
        ans.append(i)
        if not is_prime(i):
            ans.pop()
    else:
        # TODO
        return ans




if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert count_up_to(5) == [2,3], "Step 1"
    assert count_up_to(11) == [2,3,5,7], "Step 2"
    assert count_up_to(0) == [], "Step 3"
    assert count_up_to(20) == [2,3,5,7,11,13,17,19], "Step 4"
    assert count_up_to(1) == [], "Step 5"
    assert count_up_to(21) == [2,3,5,7,11,13,17,19], "Step 6"
    assert count_up_to(101) == [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97], "Step 7"
    print('Done')
