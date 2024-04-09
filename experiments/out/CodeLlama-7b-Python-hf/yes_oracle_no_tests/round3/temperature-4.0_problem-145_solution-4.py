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
    
    # 1) convert list to string
    # 2) sum the digits
    # 3) store the sum of digits in a list
    # 4) sort the list
    # 5) assign the sorted list to the original list
    
    lst = []
    for i in nums:
        lst.append(i)

    lst2 = []
    for i in lst:
        x = i
        lst2.append(sum(int(j) for j in str(x)))

    lst3 = []
    for i in lst:
        lst3.append(i)
        
    lst4 = []
    for i in lst2:
        lst4.append(i)
        
    lst4.sort()
    
    for i in range(len(lst4)):
        for j in range(len(lst2)):
            if lst4[i] == lst2[j]:
                lst3[j] = lst[j]

    return lst3


def test_function():
    assert order_by_points([1, 11, -1, -11, -12]) == [-1, -11, 1, -12, 11]
    assert order_by_points([1, -1, 2, -2, 0]) == [-2, -2, -1, 0, 1]
    assert order_by_points([]) == []
    assert order_by_points([2, 45, 99, 10, 14]) == [14, 2, 10, 45, 99]
    assert order_by_points([27, 18, 26, 12, 11]) == [11, 12, 18, 26, 27]
    assert order_by_points([-12, -11, -10, -9, -2]) == [-2, -10, -11, -12, -9]
    assert order_by_points([123, 456, 9