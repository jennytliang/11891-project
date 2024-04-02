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
    ans = 0
    for num in nums:
        digs = []
        for dig in list(str(num)):
            digs.append(int(dig))
        if num > 10:           # Odd first AND odd last number are 11,13,15,17,19
            if digs[0] % 2 == 1 and digs[-1] %2 == 1:
                ans += 1
    return ans


if __name__ == "__main__":
    print specialFilter([15, -73, 14, -15]) # 1
    print specialFilter([33, -2, -3, 45, 21, 109]) # 2
    print specialFilter([100, -16, 42, 145, 32, 91]) # 3
    print specialFilter([47, -426, 14, -15, 46, 916, 28, 3456]) # 4
    print specialFilter([47, 1, 42, 145, 32, 916, 28, 3456]) # 1
