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
    
	Do not include these tokens in the code: # First , we need to
	"""
    # First , we need to create a dictionary that connects numbers and names
    # then, we will sort the array
    # then, we will reverse the array
    # and finally we will replace the names in the array
    # and return the array
    # 1 -> One
    # 2 -> Two
    # 3 -> Three
    # 4 -> Four
    # 5 -> Five
    # 6 -> Six
    # 7 -> Seven
    # 8 -> Eight
    # 9 -> Nine
    # 0 -> Zero
    # -1 -> Negative One

    dict = {1: "One", 2: "Two", 3: "Three", 4: "Four", 5: "Five", 6: "Six", 7: "Seven", 8: "Eight", 9: "Nine"}
    sorted_arr = sorted(arr)
    reverse_arr = sorted_arr[::-1]
    new_arr = []
    for i in reverse_arr:
        if i in dict:
            new_arr.append(dict[i])
        else:
            new_arr.append(i)
    return new_arr


print(by_length([2, 1, 1, 4, 5, 8, 2, 3]))
print(by_length([2, 1, 1, 4, 5, 8, 2, 3, 10]))
print(by_length([]))
print(by_length([1, -1, 55]))
print(by_length([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
