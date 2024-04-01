def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    
	Include these tokens in the code: has _ odd , prod
	Do not include these tokens in the code: p
	"""
    # pass
    # return None
    # replace this with your code
    odd_digits = []
    for digit in str(n):
        if int(digit) % 2 == 1:
            odd_digits.append(int(digit))
    if len(odd_digits) == 0:
        return 0
    else:
        return prod(odd_digits)


def prod(nums):
    """Given a list of numbers, return the product of the numbers.
    For example:
    prod([1, 2, 3, 4]) == 24
    prod([1, 0, 1, 0]) == 0
    prod([]) == 1
    
	Include these tokens in the code: _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
	Do not include these tokens in the code: _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
	"""
    # pass
    # return None
    # replace this with your code
    if len(nums) == 0:
        return 1
    else:
        return nums[0] * prod(nums[1:])


def is_sorted(nums):
    """Given a list of numbers, return whether or not it is sorted in
    ascending order.
    For example:
    is_sorted([1, 2, 3, 4]) == True
    is_sorted([1, 3, 2, 4]) == False
	Do not include these tokens in the code: _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
	"""
    # pass
    # return None
    # replace this with your code
    for i in range(len(nums) - 1):
        if nums[i] > nums[i + 1]:
            return False
    return True

