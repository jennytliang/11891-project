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
    """
    
    if not arr:
        return []
    
    new_array = [n for n in arr if n == 1 or \
                 n == 2 or n == 3 or \
                 n == 4 or n == 5 or \
                 n == 9]
                   
    new_array = new_array[:3]
    
    for a in new_array:
        arr.pop(arr.index(a))        
    
    reverse_dict = {1: "one", 2: "two", 3: "three", \
                    4: "four", 5: "five"}

    return [reverse_dict[i].lower() for i in new_array[::-1]] + [str(i) for i in sorted(arr)]