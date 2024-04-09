def specialFilter(nums):
    """Write a function that takes an array of numbers as input and returns 
    the number of elements in the array that are greater than 10 and both 
    first and last digits of a number are odd (1, 3, 5, 7, 9).
    For example:
    specialFilter([15, -73, 14, -15]) => 1 
    specialFilter([33, -2, -3, 45, 21, 109]) => 2
    
	Include these tokens in the code: ans , odd
	Do not include these tokens in the code: # print (" special Filter ")
	"""
    ans = 0
    for i in nums:
        if i > 10:
            if i % 2 == 1:
                if i % 10 == 1 or i % 10 == 9:
                    ans += 1
    return ans


def main():
    print(specialFilter([15, -73, 14, -15]))
    print(specialFilter([33, -2, -3, 45, 21, 109]))


if __name__ == "__main__":
    main()
