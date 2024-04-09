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
	Do not include these tokens in the code: j
	"""


  ################
  #      TODO:    #
  #      YOUR CODE GOES HERE     #
  ################

  # list of all even digits
  even_digits = [2,4,6,8]

  # create empty list to store our unique list
  unique_list = []

  # loop through list of integers
  for i in x:

    # convert each integer to a string
    i_str = str(i)

    # loop through each digit in the integer
    for n in range(len(i_str)):

      # if the digit is in the even_digits list
      if int(i_str[n]) in even_digits:

        # break out of the loop
        break

      # if the digit is not in the even_digits list
      else:

        # check if the integer is already in the unique_list
        if i not in unique_list:

          # append the integer to the unique_list
          unique_list.append(i)

  # return the unique_list
  return(unique_list)


# print out result if run from command line
if __name__ == "__main__":
  print(unique_digits([15, 33, 1422, 1]))
  print(unique_digits([152, 323, 1422, 10]))