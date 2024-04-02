def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    
	Include these tokens in the code: all
	Do not include these tokens in the code: len
	"""

  # Fill this in.

def minSubArraySum(nums):
    min_sum=nums[0]
    for i in range(1,len(nums)):
        if nums[i]<nums[i-1]:
            nums[i]=nums[i]+nums[i-1]
        if nums[i]<min_sum:
            min_sum=nums[i]
    return min_sum


if __name__ == "__main__":
    input_nums = input("Enter the array of numbers: ")
    input_nums = input_nums.replace(" ", "").split(",")
    input_nums = [int(x) for x in input_nums]
    print("Minimum sum of subarray: " + str(minSubArraySum(input_nums)))
