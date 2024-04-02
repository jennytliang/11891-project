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

    # Write code here
    # 1. make variable to keep track of how many qualifying numbers
    # 2. Loop over nums using for loop, this keeps your solution flexible for 
    # different values of numLength
    # 3. Check that the number is equal to the input variable
    # 4. Then check that the first (and last) digit of that number is odd
    # 5. If answer is odd, store in variable
    
    qualifying_nums = []
    for i in nums:
        if i > 10:
            if int(i / 10) % 2 == 1 and int(i % 10) % 2 == 1:
                qualifying_nums.append(i)
            else:
                continue
    # print(qualifying_nums)   
    return len(qualifying_nums)

nums = [15, -73, 14, -15]
test_out = specialFilter(nums)
expected = 1
assert test_out == expected

nums = [33, -2, -3, 45, 21, 109]
test_out = specialFilter(nums)
expected = 2
assert test_out == expected