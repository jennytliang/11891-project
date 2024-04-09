def order_by_points(nums):
    """
    Write a function which sorts the given list of integers
    in ascending order according to the sum of their digits.
    Note: if there are several items with similar sum of their digits,
    order them based on their index in original list.

    For example:
    >>> order_by_points([1, 11, -1, -11, -12]) == [-1, -11, 1, -12, 11]
    >>> order_by_points([]) == []
    
	Include these tokens in the code: x _ list = list ( str ( x ))
	"""

    def weight(x):
  
      return sum(int(i) for i in str(x))

    nums.sort(key=weight)
    return nums


def test_function():
    assert order_by_points([1, 11, -1, -11, -12]) == [-1, -11, 1, -12, 11]
    assert order_by_points([-1, -11, 1, -12, 11]) == [-1, -11, 1, -12, 11]
    assert order_by_points([]) == []
    assert order_by_points([1]) == [1]
    assert order_by_points([1, -1]) == [-1, 1]
    assert order_by_points([1, 2, 3]) == [1, 2, 3]
    assert order_by_points([-1, -11, -12]) == [-1, -11, -12]
    assert order_by_points([111, 122, 211, 112, 121, 221]) == [111, 112, 121, 122, 211, 221]
    assert order_by_points([1, 11, 111, 21, 211, 121]) == [1, 11, 111, 121, 21, 211]
    assert order_by_points([1, 11, 111, 1111, 11111, 111111]) == [1, 11, 111, 1111, 11111, 111111]
    assert order_by_points([1, 11, 111, 1111, 11111, 111111, 1111111]) == [1, 1