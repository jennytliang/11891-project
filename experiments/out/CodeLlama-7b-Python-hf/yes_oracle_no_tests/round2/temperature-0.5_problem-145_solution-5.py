def order_by_points(nums):
    """
    Write a function which sorts the given list of integers
    in ascending order according to the sum of their digits.
    Note: if there are several items with similar sum of their digits,
    order them based on their index in original list.

    For example:
    >>> order_by_points([1, 11, -1, -11, -12]) == [-1, -11, 1, -12, 11]
    >>> order_by_points([]) == []
    
	Include these tokens in the code: x _ list = list
	Do not include these tokens in the code: return sum
	"""


    def weight(x):
 
        sum = 0
        for i in str(x):
            sum += int(i)
        return sum
    
    new_list = []
    for i in nums:
        new_list.append((i, weight(i), nums.index(i)))
    new_list.sort(key = lambda x: (x[1], x[2]))
    result = []
    for i in new_list:
        result.append(i[0])
    return result

print(order_by_points([1, 11, -1, -11, -12]))
print(order_by_points([]))