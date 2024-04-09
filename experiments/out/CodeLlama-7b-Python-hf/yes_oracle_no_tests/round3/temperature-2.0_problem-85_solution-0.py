def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    
	Include these tokens in the code: 0
	Do not include these tokens in the code: ""
	"""

  
    # code goes here
    return sum(lst[1::2])


# Simple provided test() function used in main() to print
# what each function returns vs. what it's supposed to return.
def test(got, expected):
  if got == expected:
    prefix = ' OK '
  else:
    prefix = '  X '
  print '%s got: %s expected: %s' % (prefix, repr(got), repr(expected))


# Calls the above functions with interesting inputs.
def main():
  print 'add'
  test(add([4, 2, 6, 7]), 2)
  test(add([4, 0, 6, 7]), 6)
  test(add([4, 0, 10, 7]), 14)


if __name__ == '__main__':
  main()