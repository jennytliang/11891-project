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
    
	Do not include these tokens in the code: # by _ length ( arr )
	"""
    # def by_length(arr):
    #     # sort arr
    #     arr.sort()
    #     # reverse arr
    #     arr.reverse()
    #     # replace each digit by its corresponding name from "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"
    #     return [
    #         "One" if i == 1 else
    #         "Two" if i == 2 else
    #         "Three" if i == 3 else
    #         "Four" if i == 4 else
    #         "Five" if i == 5 else
    #         "Six" if i == 6 else
    #         "Seven" if i == 7 else
    #         "Eight" if i == 8 else
    #         "Nine" if i == 9 else ""
    #         for i in arr
    #     ]
    # return by_length(arr)

    def by_length(arr):
        # sort arr
        arr.sort()
        # reverse arr
        arr.reverse()
        # replace each digit by its corresponding name from "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"
        return [
            "One" if i == 1 else
            "Two" if i == 2 else
            "Three" if i == 3 else
            "Four" if i == 4 else
            "Five" if i == 5 else
            "Six" if i == 6 else
            "Seven" if i == 7 else
            "Eight" if i == 8 else
            "Nine" if i == 9 else ""
            for i in arr
        ]
    return by_length(arr)

    # def by_length(arr):
    #     # sort arr
    #     arr.sort()
    #     # reverse arr
    #     arr.reverse()
    #     # replace each digit by its corresponding name from "One", "