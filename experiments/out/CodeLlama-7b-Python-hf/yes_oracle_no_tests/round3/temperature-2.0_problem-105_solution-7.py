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
    # write your code here
    import numpy as np
    from numpy.lib.function_base import select
    arr = np.array(arr)
    arr[arr > 9] = 0
    arr[arr < 1] = 0
    arr[arr == 0] = 9
    arr[arr == 9] = 1
    arr = np.sort(arr)
    arr = arr[::-1]
    arr = arr.astype(str)
    arr = arr.tolist()
    arr = list(map(str, arr))
    arr = list(map(lambda x: "One" if str(x) == "1" else "Two" if str(x) == "2" else "Three" if str(x) == "3" else "Four" if str(x) == "4" else "Five" if str(x) == "5" else "Six" if str(x) == "6" else "Seven" if str(x) == "7" else "Eight" if str(x) == "8" else "Nine" if str(x) == "9" else "", arr))
    return arr


# print(by_length([2, 1, 1, 4, 5, 8, 2, 3]))
# print(by_length([]))
# print(by_length([1, -1, 55]))
print(by_length([1, 2, 3, 4, 5, 6, 7, 8, 9]))
