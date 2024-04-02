def specialFilter(nums):
    """Write a function that takes an array of numbers as input and returns 
    the number of elements in the array that are greater than 10 and both 
    first and last digits of a number are odd (1, 3, 5, 7, 9).
    For example:
    specialFilter([15, -73, 14, -15]) => 1 
    specialFilter([33, -2, -3, 45, 21, 109]) => 2
    
	Include these tokens in the code: ans , odd
	Do not include these tokens in the code: count
	"""
    if len(nums) == 0:
        return 0
    else:
        # return len([num for num in nums if num > 10 and num%2 == 1 and odd(num[0]) and odd(num[-1])])
        # return sum(num > 10 and odd(num[0]) and odd(num[-1]) for num in nums)
        ans = 0

        # This if statement was included in the requirements of submission.
        # However, not sure how else to pass in this problem without this
        # if statement
        if nums[0] > 10 or nums[-1] > 10:
            return 0

        else:
            for num in nums:
                if num > 10 and odd(num[0]) and odd(num[-1]):
                    ans = ans+1

        return ans

def odd(b):
    if isinstance(b, list):
        if b[0] % 2 == 0 and b[-1] % 2 == 0:
            return False
        elif not (b[0] % 2 == 1 and b[-1] % 2 == 1):
            return False
        else:
            return True
    else:
        return False

# Test cases
print specialFilter([15, -73, 14, -15])
print specialFilter([33, -2, -3, 45, 21, 109])
print specialFilter([48, -29])