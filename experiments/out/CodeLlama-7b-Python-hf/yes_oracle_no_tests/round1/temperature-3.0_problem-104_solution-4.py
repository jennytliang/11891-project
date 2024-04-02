def unique_digits(x):
    """Given a list of positive integers x. return a sorted list of all 
    elements that hasn't any even digit.

    Note: Returned list should be sorted in increasing order.
    
    For example:
    >>> unique_digits([15, 33, 1422, 1])
    [1, 15, 33]
    >>> unique_digits([152, 323, 1422, 10])
    []
    
	Include these tokens in the code: judge
	Do not include these tokens in the code: has _ even _ digit
	"""


  # Write your code below this line
  pass

  # Write your code above this line


#  DO NOT EDIT CODE BELOW THIS LINE 
if __name__ == '__main__':
  assert unique_digits([15, 33, 1422, 1]) == [1, 15, 33], "Wrong Output"
  assert unique_digits([152, 323, 1422, 10]) == [], "Wrong Output"
  assert unique_digits([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == [], "Wrong Output"
  assert unique_digits([100, 100, 100]) == [], "Wrong Output"
  assert unique_digits([100, 100, 100, 100]) == [], "Wrong Output"
  assert unique_digits([1000, 2000, 3000, 4000]) == [], "Wrong Output"
  assert unique_digits([10000, 20000, 30000, 40000]) == [], "Wrong Output"
  assert unique_digits([100000, 200000, 300000, 400000]) == [], "Wrong Output"
  assert unique_digits([1000000, 2000000, 3000000, 4000000]) == [], "Wrong Output"
  assert unique_digits([10000000, 20000000, 30000000, 40000000]) == [], "Wrong Output"
  assert unique_digits([100000000, 200000000, 300000000,