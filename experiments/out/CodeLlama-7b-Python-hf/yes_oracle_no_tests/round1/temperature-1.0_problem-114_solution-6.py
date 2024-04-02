def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    
	Include these tokens in the code: if all ( x >=
	"""
    if len(nums) < 2:
        return sum(nums)  # if array is empty or has only 1 element, return sum

    smallest, sum_so_far = float("inf"), float("-inf")

    for num in nums:
        if num < smallest:  # update smallest element
            smallest = num
        sum_so_far += num
        if sum_so_far > 0:  # since array has more than 1 element
            sum_so_far = sum_so_far - smallest  # subtract smallest element, which has negative value

    return sum_so_far


print(minSubArraySum([2, 3, 5, 5, 4, 1, 2]))  # 6


"""
def minSubArraySum(nums):
    min_in_window = max_in_window = float("inf")
    min_idx_in_window = max(len(nums), 0)
    result = []
    for i in range(len(nums)):
        if max_in_window < min_in_window*nums[i]:
            min_idx_in_window = i

        max_in_window = max(max_in_window, nums[i])
        min_in_window = min(min_in_window, nums[i])

        if (max_in_window - min_in_window) < min_idx_in_window:
            result.append(nums[min_idx_in_window:max_in_window])
            print(min_idx_in_window, result)
    return result
    
print(minSubArraySum([2, 3, 4, 1, 2, 4]))  # [1, 2, 4]
"""



########
"""
var nums = [2, 11, 3, 12, 5, 21, 11];

var minSubArraySum = function(nums) {
    if (nums.length == 0){
        return 0