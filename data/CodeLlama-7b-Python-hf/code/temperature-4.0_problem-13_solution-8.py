def greatest_common_divisor(a: int, b: int) -> int:
    """ Return a greatest common divisor of two integers a and b
    >>> greatest_common_divisor(3, 5)
    1
    >>> greatest_common_divisor(25, 15)
    5
    """

    if a < b:
        return a
    else:
        return  greatest_common_divisor(a - b, b )
    
print(f'Result of 4, 12:                           {greatest_common_divisor(4, 12)}') 
if greatest_common_divisor(4, 12) == 4:
    print('Result 4, and the greatest divisor are equal, 4')
# if greatest_common_divisor(4, 28) == 4:          14 - 6 = ?


def gcd(a, b): 
  """ Calculate the greatest common denominator of two positive integers
      Calculate the greatest common denominator in Python using recursion
      a> 0 b > 0
  """

  smallerNumber =  a    
  if a == b: print("Error : a must be striclty smaller than b")  

  while a != b:

      if a > b: 
        a - b

