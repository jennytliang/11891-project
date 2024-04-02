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

  nums2 = []
  submin2 = 99999 #99999
  
  nums3 = []
  
  i = 0;
  for elem in range(0, len(nums)):
      nums2.append(nums[i] + nums[i+1])
      i +=2
      print(nums2)
     
  print(nums2)
  for ele in nums:
      nums3.append(ele*2)
     
  for ix in nums2:
      if ix < submin2:
          submin2 = ix
          
  print(submin2)
  return submin2
  
minSubArraySum([2, 3, 4, 1, 2, 4])