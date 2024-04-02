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


  # =============================================================================
  #   This is a brute force solution. It will work but it will take a lot of 
  #   time for large numbers.
  # 
  #   Try to solve this problem using the following hint.
  # 
  #   Use the following function in your code:
  #   def has_even_digit(x):
  #       
  # =============================================================================
    even_digits = set()
    for i in range(x):
        if not str(i).__contains__('2') or not str(i).__contains__('4') or not str(i).__contains__('6') or not str(i).__contains__('8'):
            even_digits.add(i)
    return sorted(even_digits)



def unique_digits_2(x):
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

  # =============================================================================
  #   Use the following function in your code:
  #   def has_even_digit(x):
  #       
  # =============================================================================
    even_digits = set()
    for i in range(x):
        if not str(i).__contains__('2') or not str(i).__contains__('4') or not str(i).__contains__('6') or not str(i).__contains__('8'):
            even_digits.add(i)
    return sorted(even_digits)



def unique