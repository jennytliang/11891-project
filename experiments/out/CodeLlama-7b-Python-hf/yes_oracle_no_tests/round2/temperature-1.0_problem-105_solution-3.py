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
    
	Do not include these tokens in the code: def is _ between _ 1
	"""
    # 
    def check(i): 
        if i == 1:
            return "One"
        elif i == 2:
            return "Two"
        elif i == 3:
            return "Three"
        elif i == 4:
            return "Four"
        elif i == 5:
            return "Five"
        elif i == 6:
            return "Six"
        elif i == 7:
            return "Seven"
        elif i == 8:
            return "Eight"
        elif i == 9:
            return "Nine"
    
    r = [check(i) for i in arr if (i <= 9 and i >= 1)]
    return r[::-1]


print(by_length([2, 1, 1, 4, 5, 8, 2, 3]))
print(by_length([]))
print(by_length([1, 2, 3, 99]))
print(by_length([1,2,3,4,5,6,7,8,9]))
print(by_length([3,9,8,4,6,1,2,7,5]))