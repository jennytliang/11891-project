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
	Do not include these tokens in the code: # TODO : Write your code here
	"""
    # TODO : Write your code here
    result = []
    
    for i in range(len(arr)):
        if arr[i] >= 1 and arr[i] <= 9:
            result.append(str(arr[i]))
    
    result.sort()
    result.reverse()
    
    for i in range(len(result)):
        if result[i] == "1":
            result[i] = "One"
        elif result[i] == "2":
            result[i] = "Two"
        elif result[i] == "3":
            result[i] = "Three"
        elif result[i] == "4":
            result[i] = "Four"
        elif result[i] == "5":
            result[i] = "Five"
        elif result[i] == "6":
            result[i] = "Six"
        elif result[i] == "7":
            result[i] = "Seven"
        elif result[i] == "8":
            result[i] = "Eight"
        elif result[i] == "9":
            result[i] = "Nine"
    
    return result


print(by_length([2, 1, 1, 4, 5, 8, 2, 3]))
print(by_length([]))
print(by_length([1, -1 , 55]))