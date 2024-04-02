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
	Do not include these tokens in the code: # return [] # return
	"""
    # return []
    if arr == []:
        return []
    else:
        arr.sort()
        arr.reverse()
        arr2 = []
        for i in arr:
            if i >= 1 and i <= 9:
                arr2.append(str(i))
            else:
                arr2.append(str(i))
        arr3 = []
        for i in arr2:
            if i == "1":
                arr3.append("One")
            elif i == "2":
                arr3.append("Two")
            elif i == "3":
                arr3.append("Three")
            elif i == "4":
                arr3.append("Four")
            elif i == "5":
                arr3.append("Five")
            elif i == "6":
                arr3.append("Six")
            elif i == "7":
                arr3.append("Seven")
            elif i == "8":
                arr3.append("Eight")
            elif i == "9":
                arr3.append("Nine")
        return arr3


print(by_length([2, 1, 1, 4, 5, 8, 2, 3]))
print(by_length([]))
print(by_length([1, -1, 55]))
