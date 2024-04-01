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
    #
    # Solution:
    #
    # 1.  Sort the array, reverse it, and convert to string.
    # 2.  Convert the strings to ints, and use a dictionary to map the ints to the words.
    # 3.  Return the words as a list.
    #
    #   def by_length(arr):
    #       if not arr:
    #           return []
    #       
    #       arr = sorted(arr, reverse=True)
    #       arr = list(map(str, arr))
    #       words = {
    #           '1': 'One',
    #           '2': 'Two',
    #           '3': 'Three',
    #           '4': 'Four',
    #           '5': 'Five',
    #           '6': 'Six',
    #           '7': 'Seven',
    #           '8': 'Eight',
    #           '9': 'Nine'
    #       }
    #       return list(map(words.get, arr))

    def to_word(x):
        words = {
            '1': 'One',
            '2': 'Two',
            '3': 'Three',
            '4': 'Four',
            '5': 'Five',
            '6': 'Six',
            '7': 'Seven',
            '8': 'Eight',
            '9': 'Nine'
        }
        return words.get(str(x))

    if arr == []:
        return []
    
    arr = sorted(arr, reverse=True)
    arr = list(map(str, arr))
    
    return list(map(to_word, arr))

    # return arr


print(by_length([2, 1, 1, 4, 5, 8, 2, 3]))
print(by_length([1, 2, 3, 4, 5, 6, 7, 8, 9]))
print(by_length([1, 2, 3, 