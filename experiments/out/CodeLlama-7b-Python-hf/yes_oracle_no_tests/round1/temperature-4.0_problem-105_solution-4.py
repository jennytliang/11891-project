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

    # First, we need to sort the array
    arr.sort()

    # We need to check if the array is empty
    if len(arr) == 0:
        return []

    # We need to check if the array has any strange number
    if arr[0] < 1 or arr[-1] > 9:
        arr = [x for x in arr if x in range(1, 10)]
        if len(arr) == 0:
            return []

    # We need to reverse the array
    arr.reverse()

    # We need to get the name of each number
    def to_word(x):
        if x == 1:
            return "One"
        elif x == 2:
            return "Two"
        elif x == 3:
            return "Three"
        elif x == 4:
            return "Four"
        elif x == 5:
            return "Five"
        elif x == 6:
            return "Six"
        elif x == 7:
            return "Seven"
        elif x == 8:
            return "Eight"
        else:
            return "Nine"

    # We need to get the name of each number
    result = []
    for i in arr:
        result.append(to_word(i))

    return result


# print(by_length([2, 1, 1, 4, 5, 8, 2, 3]))
# print(by_length([]))
# print(by_length([1, -1, 55]))
# print(by_length([1, 1, 2, 2, 3, 4, 5, 8]))
print(by_length([2, 1, 1, 4, 5, 8, 2, 3, 10, 11, 12]))
