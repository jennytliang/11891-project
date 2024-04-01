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

    # We'll do this with list comprehensions
    # First, sort the array
    arr = sorted(arr)
    # Then, reverse the array
    arr.reverse()
    # Create a list of the names
    names = ["One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
    # Create a list of the numbers
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    # Create an empty list to store the names
    word_arr = []
    # Loop through the array
    for x in arr:
        # If the element is between 1 and 9 inclusive, append the word to the list
        if x in numbers:
            word_arr.append(names[numbers.index(x)])
        # If the element is not between 1 and 9 inclusive, ignore it
        else:
            continue
    # Return the list of words
    return word_arr


# print(by_length([2, 1, 1, 4, 5, 8, 2, 3]))
# print(by_length([]))
# print(by_length([1, -1, 55]))
