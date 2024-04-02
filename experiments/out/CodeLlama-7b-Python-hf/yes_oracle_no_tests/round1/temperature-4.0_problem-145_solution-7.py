def order_by_points(nums):
    """
    Write a function which sorts the given list of integers
    in ascending order according to the sum of their digits.
    Note: if there are several items with similar sum of their digits,
    order them based on their index in original list.

    For example:
    >>> order_by_points([1, 11, -1, -11, -12]) == [-1, -11, 1, -12, 11]
    >>> order_by_points([]) == []
    
	Include these tokens in the code: weight
	Do not include these tokens in the code: sort
	"""


  # BEGIN PROBLEM 1
    sorted_nums = []
    for num in nums:
        if num < 0:
            sum_of_digits = sum([int(digit) for digit in str(num)])
            if not sorted_nums:
                sorted_nums.append(num)
            else:
                for i in range(len(sorted_nums)):
                    if sum_of_digits > sum(sorted_nums[i]):
                        sorted_nums.insert(i, num)
                        break
                    elif sum_of_digits == sum(sorted_nums[i]):
                        sorted_nums.insert(i+1, num)
                        break
                else:
                    sorted_nums.append(num)
        else:
            sum_of_digits = sum([int(digit) for digit in str(num)])
            if not sorted_nums:
                sorted_nums.append(num)
            else:
                for i in range(len(sorted_nums)):
                    if sum_of_digits > sum(sorted_nums[i]):
                        sorted_nums.insert(i, num)
                        break
                    elif sum_of_digits == sum(sorted_nums[i]):
                        sorted_nums.insert(i+1, num)
                        break
                else:
                    sorted_nums.append(num)
    return sorted_nums
  # END PROBLEM 1



def order_by_points_2(nums):
  """
  Write a function which sorts the given list of integers
  in ascending order according to the sum of their digits.
  Note: if there are several items with similar sum of their digits,
  order them based on their index in original list.

  For example:
  >>> order_by_points([1, 11, -1, -11, -12]) == [-1, -11, 1, -12, 11]
  >>> order_by_points([