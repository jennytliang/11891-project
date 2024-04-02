def count_nums(arr):
    """
    Write a function count_nums which takes an array of integers and returns
    the number of elements which has a sum of digits > 0.
    If a number is negative, then its first signed digit will be negative:
    e.g. -123 has signed digits -1, 2, and 3.
    >>> count_nums([]) == 0
    >>> count_nums([-1, 11, -11]) == 1
    >>> count_nums([1, 1, 2]) == 3
    
	Include these tokens in the code: def judge ( x : int ) -> int :
	"""

    "*** YOUR CODE HERE ***"
    count = 0
    num = 0
    for x in arr:
        if x < 0:
            num = -1 * int(str(abs(x))[0])
        else:
            num = int(str(abs(x))[0])
        sum_num = sum(int(a) for a in str(x))
        count += 1 if (num > sum_num) else 0
    return count
    

def remove_smallest(nums):
    "*** YOUR CODE HERE ***"
    "Return a copy of the list, should not change the original."
    "*** YOUR CODE HERE ***"
    "If there are multiple minimum values in the list, remove all of the minimum values."
    new_nums = nums[:] 
    if len(new_nums) > 0:
        minimum = new_nums[0]
        for i in range(len(new_nums)):
            if minimum > new_nums[i]:
                minimum = new_nums[i]
        for j in range(len(new_nums)):
            if minimum == nums[j]:
                new_nums.pop(j)
    return new_nums
