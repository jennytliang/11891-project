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
    
	Include these tokens in the code: : int ) -> str :
	Do not include these tokens in the code: ):
	"""

    def to_w(num):
        if num == 1:
            return "One"
        elif num == 2:
            return "Two"
        elif num == 3:
            return "Three"
        elif num == 4:
            return "Four"
        elif num == 5:
            return "Five"
        elif num == 6:
            return "Six"
        elif num == 7:
            return "Seven"
        elif num == 8:
            return "Eight"
        elif num == 9:
            return "Nine"

    def by_len(arr):
        if len(arr) == 0:
            return []
        else:
            arr.sort()
            arr.reverse()
            arr2 = []
            for i in arr:
                if i > 0 and i < 10:
                    arr2.append(to_w(i))
            return arr2

    return by_len(arr)


# print(by_length([2, 1, 1, 4, 5, 8, 2, 3]))
# print(by_length([1, -1, 55]))
# print(by_length([]))
