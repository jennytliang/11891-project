def by_length(arr):
    """
    Given an array of integers, sort the integers that are between 1 and 9 inclusive,
    reverse the resulting array, and then replace each digit by its corresponding name from
    "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine".

    For example:
      arr = [2, 1, 1, 4, 5, 8, 2, 3]   
            -> sort arr -> [1, 1, 2, 2, 3, 4, 5, 8] 
            -> reverse arr -> [8, 5, 4, 3, 2, 2, 1, 1]
      return ["Eight", "Five", "Four", "Three", "Two", "Two", "One", "One"]
    
      If the array is empty, return an empty array:
      arr = []
      return []
    
      If the array has any strange number ignore it:
      arr = [1, -1 , 55] 
            -> sort arr -> [-1, 1, 55]
            -> reverse arr -> [55, 1, -1]
      return = ['One']
    
	Include these tokens in the code:  def to _ word ( x : int
	"""

    # sort the arr
    arr.sort()

    # reverse the arr
    arr.reverse()

    # define the word dictionary
    words = {
        1: "One",
        2: "Two",
        3: "Three",
        4: "Four",
        5: "Five",
        6: "Six",
        7: "Seven",
        8: "Eight",
        9: "Nine",
    }

    # create an empty arr for the words
    words_arr = []

    # for loop to iterate through the arr
    for i in arr:
        # if statement to check if the number is between 1 and 9 inclusive
        if i >= 1 and i <= 9:
            # append the words to the words_arr
            words_arr.append(words[i])
        # else statement to return empty arr
        else:
            return []

    # return the words_arr
    return words_arr


# arr = [2, 1, 1, 4, 5, 8, 2, 3]
# print(by_length(arr))
