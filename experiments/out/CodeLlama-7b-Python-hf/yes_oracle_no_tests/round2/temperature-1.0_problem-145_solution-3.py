def order_by_points(nums):
    """
    Write a function which sorts the given list of integers
    in ascending order according to the sum of their digits.
    Note: if there are several items with similar sum of their digits,
    order them based on their index in original list.

    For example:
    >>> order_by_points([1, 11, -1, -11, -12]) == [-1, -11, 1, -12, 11]
    >>> order_by_points([]) == []
    
	Include these tokens in the code: def weight ( x ): x _ list
	"""
         

    result = sorted(nums, key=lambda x: (sum(list(map(lambda d: int(d),
                                                      str(x)))), x)) 
    
    return result


def order_by_points2(nums):
    """
    Write a function which sorts the given list of integers
    in ascending order according to the sum of their digits.
    Note: if there are several items with similar sum of their digits,
    order them based on their index in original list.

    For example:
    >>> order_by_points([1, 11, -1, -11, -12]) == [-1, -11, 1, -12, 11]
    >>> order_by_points([]) == []
    
	Include these tokens in the code: def weight ( x ): x _ list
	"""
            
    new = sorted([{num: sum([int(x) for x in str(num)])} for num in nums], key=lambda x: (
        x[next(iter(x))], next(iter(x)))) 
    result = [x[index] for x in new for index in x][::-1] 
    return result
         
    

if __name__ == '__main__':
    print(order_by_points([1, 11, -1, -11, -12]))
    print(order_by_points2([1, 11, -1, -11, -12]))
    
    
    
    
