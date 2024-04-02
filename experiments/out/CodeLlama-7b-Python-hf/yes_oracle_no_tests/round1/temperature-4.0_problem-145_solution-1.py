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


  # write your code here
    a=[]
    for i in range(len(nums)):
        a.append([sum(int(x) for x in str(nums[i])),i,nums[i]])
    a.sort()
    return [a[i][2] for i in range(len(a))]






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


  # write your code here
    a=[]
    for i in range(len(nums)):
        a.append([sum(int(x) for x in str(nums[i])),i,nums[i]])
    a.sort()
    return [a[i][2] for i in range(len(a))]







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


  # write your code here
   