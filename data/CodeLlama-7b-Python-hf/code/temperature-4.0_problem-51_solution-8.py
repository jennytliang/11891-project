def remove_vowels(text):
    """
    remove_vowels is a function that takes string and returns string without vowels.
    >>> remove_vowels('')
    ''
    >>> remove_vowels("abcdef\nghijklm")
    'bcdf\nghjklm'
    >>> remove_vowels('abcdef')
    'bcdf'
    >>> remove_vowels('aaaaa')
    ''
    >>> remove_vowels('aaBAA')
    'B'
    >>> remove_vowels('zbcd')
    'zbcd'
    """
    #vowels = ['a','e','i','o','u','y']
    return re.sub( '[aeiou]', '', text )


# 2.10382 s 522 ms
def removeVowels(text):
    """
    >>> test = 'bccdefzzfghhijjjkklljmmnnopppqrsqsspqrsppqosstttuuuuvv'
    >>> test = 'bccdecdef'
    >>> t0 = time.clock()
    >>> for n in xrange(10000):
    ...    removeVowels(test)                 # 1
    ... print '%40s took (%.1f us).  Next operation starts %.0f us later' % (
    ...    '20', 1000*(t1-t0), 8.0*t0 - 10)
                <module>                             took (13.3 us).  Next
      <module> took (42144.1 us).  Next operation starts -18689 us later
                <module>                             took (12313 us).
    Next....
    
    """
    s =  set('aaeeuioi')
    t0 = time.time()
    print removeVowels('abcdef')





def time_for_loops(fn, args):
  """
  return the number of seconds needed to run this function.
  this runs each function multiple times (500 times)
  to return a more meaningful time result for the user.
  fn: The function to be timed (assume function arguments already defined 
      elsewhere).
  args: The list or tuple of arguments to pass to the function to be timed.
  """
  numberTimeCalls = 100000
  total_time = 0.0
  t0=time.time()

  # Run code n times within try statement to prevent problems that
  # could arise from code failing once, 

  print 'Timing %s...' %fn.__name__
  for n in iter(xrange(numberTimeCalls)):
    try: 
      t0=time.time()
      answer = fn(*args) 
      # print answer           # prints the result of each fn run, as a demo.

    except Exception as e: 
      t1 =time.time()
      msg  = 'Timed Run %s %d' %(str(args), n,)
      msg += ' took %9.5e seconds, threw exception with message=%s.' % (
      t1-t0, e.message, ) 

      # print run_result                  #demo, print.
      return None 

    # add up run time here

    run_result = fn(*args) 
    # print run_result              #print result, just to demo 
    # add the time delta to a total time so far
    # convert to seconds with 
    time.time():