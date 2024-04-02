def order_by_points(nums):
    """
    Write a function which sorts the given list of integers
    in ascending order according to the sum of their digits.
    Note: if there are several items with similar sum of their digits,
    order them based on their index in original list.

    For example:
    >>> order_by_points([1, 11, -1, -11, -12]) == [-1, -11, 1, -12, 11]
    >>> order_by_points([]) == []
    
	Include these tokens in the code: def weight ( x ):
	"""
    def weight(x):
        return sum(int(i) for i in str(x))
    
    return sorted(nums, key=lambda x: (weight(x), x))
    

def test_function():
    assert order_by_points([1, 11, -1, -11, -12]) == [-1, -11, 1, -12, 11]
    assert order_by_points([1, 11, -1, -11, -12, 100]) == [-1, -11, 1, -12, 11, 100]
    assert order_by_points([]) == []
    assert order_by_points([1]) == [1]
    assert order_by_points([-100, 1, 100]) == [-100, 1, 100]
    assert order_by_points([-100, 1, 100, -1000, 1000]) == [-100, 1, -1000, 100, 1000]
    assert order_by_points([-100, -1000, 100, 1000]) == [-100, -1000, 100, 1000]
    assert order_by_points([-1000, 1000, 1, -1000]) == [-1000, -1000, 1000, 1]

if __name__ == '__main__':
    test_function()
