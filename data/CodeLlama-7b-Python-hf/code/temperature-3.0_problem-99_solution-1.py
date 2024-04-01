def closest_integer(value):
    '''
    Create a function that takes a value (string) representing a number
    and returns the closest integer to it. If the number is equidistant
    from two integers, round it away from zero.

    Examples
    >>> closest_integer("10")
    10
    >>> closest_integer("15.3")
    15

    Note:
    Rounding away from zero means that if the given number is equidistant
    from two integers, the one you should return is the one that is the
    farthest from zero. For example closest_integer("14.5") should
    return 15 and closest_integer("-14.5") should return -15.
    '''
    # your code here
    
    if value in ("-0", "-0.0", "0", "0.0"):
      return 0

    if value in ("1", "1.0"):
      return 1
    
    if "." in value:
      val = round(float(value))
    else:
      val = float(value)

    is_even = bool(val % 2 == 0)
    
    if val % 1 == 0:
      return int(val)
    else:
      if (val > 0 and is_even) or (val < 0 and not is_even):
        return int(val) + 1
      else:
        return int(val)