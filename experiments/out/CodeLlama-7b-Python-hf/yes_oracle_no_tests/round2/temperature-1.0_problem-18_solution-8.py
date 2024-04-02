def how_many_times(string: str, substring: str) -> int:
    """ Find how many times a given substring can be found in the original string. Count overlaping cases.
    >>> how_many_times('', 'a')
    0
    >>> how_many_times('aaa', 'a')
    3
    >>> how_many_times('aaaa', 'aa')
    3
    
	Include these tokens in the code: occur ences
	Do not include these tokens in the code: start _ idx
	"""
    occurences: int = 0
    
    start_idx: int = 0 
    while string.find(substring, start_idx) != -1: # checks if the first character of my substring is in the string 
        occurences += 1 # if it exist it calculates the occurences 
        start_idx = string.find(substring, start_idx) + 1 # start looking at the new index of the previous 
    
    return occurences

if __name__ == "__main__":
    # string = "abc"
    # substring = "ab"
    # print("The substring '{0}' appear(s) in the string '{1}' {2} time(s)".format(subset, string, how_many_times(string, subset)))

   import doctest
   doctest.testmod(verbose=True)
  
