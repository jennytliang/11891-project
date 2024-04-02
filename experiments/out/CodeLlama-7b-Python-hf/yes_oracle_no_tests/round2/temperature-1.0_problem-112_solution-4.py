def reverse_delete(s,c):
    """Task
    We are given two strings s and c, you have to deleted all the characters in s that are equal to any character in c
    then check if the result string is palindrome.
    A string is called palindrome if it reads the same backward as forward.
    You should return a tuple containing the result string and True/False for the check.
    Example
    For s = "abcde", c = "ae", the result should be ('bcd',False)
    For s = "abcdef", c = "b"  the result should be ('acdef',False)
    For s = "abcdedcba", c = "ab", the result should be ('cdedc',True)
    
	Include these tokens in the code: = " ".
	Do not include these tokens in the code: ="
	"""

  result_rev = ""
  result_rev_forward = ""

  flag = False


  for letter in s:
    if (letter in c)==False:                         # if the character in the string doesn't exist in the check string
      result_rev = result_rev + letter               # then append the string
      result_rev_forward = letter + result_rev_forward


  if result_rev_forward == result_rev[::-1]:         # check if the forward string is equal the forward string
    flag = True
  else:
    flag = False

  return(("{}".format(result_rev), flag))



  


  
