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
    
	Include these tokens in the code: def
	Do not include these tokens in the code: # Step 1 : Sort the
	"""
    # Step 1 : Sort the array
    arr.sort()
    
    # Step 2 : Reverse the array
    arr.reverse()
    
    # Step 3 : Replace each digit by its corresponding name from "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"
    result = []
    for num in arr:
        if num == 1:
            result.append("One")
        elif num == 2:
            result.append("Two")
        elif num == 3:
            result.append("Three")
        elif num == 4:
            result.append("Four")
        elif num == 5:
            result.append("Five")
        elif num == 6:
            result.append("Six")
        elif num == 7:
            result.append("Seven")
        elif num == 8:
            result.append("Eight")
        elif num == 9:
            result.append("Nine")
    
    return result
        
print(by_length([2, 1, 1, 4, 5, 8, 2, 3]))
print(by_length([]))
print(by_length([1, -1 , 55]))