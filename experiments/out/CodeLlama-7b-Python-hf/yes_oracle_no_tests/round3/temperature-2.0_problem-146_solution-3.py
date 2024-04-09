def specialFilter(nums):
    """Write a function that takes an array of numbers as input and returns 
    the number of elements in the array that are greater than 10 and both 
    first and last digits of a number are odd (1, 3, 5, 7, 9).
    For example:
    specialFilter([15, -73, 14, -15]) => 1 
    specialFilter([33, -2, -3, 45, 21, 109]) => 2
    
	Include these tokens in the code: ans , odd =
	"""
    # Initialize variables
    ans = 0
    odd = False

    # Iterate through elements in list
    for i in nums:
        # Check if element is greater than 10
        if i > 10:
            # Check if first and last digits are odd
            if i % 10 in [1, 3, 5, 7, 9]:
                # Increment counter
                ans += 1

    # Print number of elements in array that are greater than 10 and both first and last digits are odd
    print(ans)


def main():
    # Get input from user
    nums = eval(input("Enter list of numbers: "))
    
    # Run specialFilter function
    specialFilter(nums)


if __name__ == "__main__":
    main()
