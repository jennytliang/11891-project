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
    # print('by_length')
    
    ## EDGE CASES ##
    if len(arr) == 0:
        return ""
    else:
        # print('Edge cases passed')
        if len(arr) == 0:
            return []
    
        
        digits = {1: "One", 2: "Two", 3: "Three", 4: "Four", 5: "Five", 6: "Six", 7: "Seven", 8: "Eight", 9: "Nine"}
        
        # print(arr)
    
        filtered_arr = [i for i in arr if i >= 1 and i <= 9]
        # print(filtered_arr)
        # filtered_arr = arr
        while 0 in filtered_arr:
            filtered_arr.pop(filtered_arr.index(0))
        # print(filtered_arr)
        sorted_arr = sorted(filtered_arr, reverse=True)
        # print(sorted_arr)
        # new_arr = [digits[x] for x in filtered_arr]
        new_arr = []
        for num in sorted_arr:
            if num > 0 and num <= 9:
                new_arr.append(digits[num])
            # else:
                # new_arr.append(digits[num])
        # print(new_arr)
        return new_arr
        
def sort_list(arr, ascending=True):
    """
    Given an array of integers, return the indices of its sorted values using the built-in .sort() method.

	Example:
	  sort_list(list_of_int) -> [4, 2, 0, 1]
    """
    
    ## EDGE CASES ##
    if len(arr) == 0:
        return ""

        if len(arr) == 0:
            return []
    
    if ascending:
        arr.sort()
        sorted_arr = [x for x, _ in enumerate(arr)]
        return sorted_arr
    
    if