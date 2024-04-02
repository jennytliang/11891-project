def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    
	Include these tokens in the code: s = str ( x )
	"""
    if shift > len(str(x)):
        lst = list(str(x)[::-1])
    else:
        lst = list(str(x))
    try:
      lst = lst[shift:] + lst[:shift]
      return ''.join(lst)
    except IndexError:
      return 'Please include a positive number for circular shift'
    
print(circular_shift(12, 1))
print(circular_shift(12, 2))
    
    
def circular_shift(x, shift):
    lst = list(str(x))
    shift = shift % len(lst)
    if shift == 0:
        return x
    if shift < 0:
        lst = lst[::-1]
    new_lst = lst[-shift:] + lst[:-shift]
    return int("".join(reversed(new_lst)))
print(circular_shift(42, -5))
print(circular_shift(1337, 4))
print(circular_shift(-273, 7))