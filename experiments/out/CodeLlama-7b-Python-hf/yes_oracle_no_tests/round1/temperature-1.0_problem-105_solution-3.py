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
    
	Include these tokens in the code: def to _ word ( x : int ) ->
	"""

    def is_between_1_and_9(x):
        return 0 < x < 10

    def to_word(x):
        return ('One', 
                'Two', 
                'Three', 
                'Four', 
                'Five', 
                'Six', 
                'Seven', 
                'Eight',
                'Nine')[x-1]


    # Implement the by_length() function here!
    words = []
    # Make a shallow copy of the list 
    newArr = []
    newArr[:0] = arr
    arr = newArr
    # Sort the list
    arr.sort(reverse=True)
    # Reverse the list
    arr.reverse()
    # Map each entry according to the given function and push it to result array
    for elem in arr:
        # Reverse the function to handle decimals appropriately
        if is_between_1_and_9(elem) and elem >= 1 and elem <= 9:
            words.append(str(to_word(elem)))
            # print(elem)
    # Print the result
    return words

# List of integers
print(by_length([1,5,2,3]))
# Integer
print(by_length(2))
# Empty list
print(by_length([])) 
# Weird numbers array
print(by_length([1,2,3,0,-5]))
print(by_length([1,2,3,0,-5,10,-7]))