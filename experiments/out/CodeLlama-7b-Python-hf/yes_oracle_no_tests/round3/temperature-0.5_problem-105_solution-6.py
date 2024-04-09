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

    def to_w(i):
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

    def to_i(i):
        if i == "One":
            return 1
        elif i == "Two":
            return 2
        elif i == "Three":
            return 3
        elif i == "Four":
            return 4
        elif i == "Five":
            return 5
        elif i == "Six":
            return 6
        elif i == "Seven":
            return 7
        elif i == "Eight":
            return 8
        elif i == "Nine":
            return 9

    def by_length(arr):
        if len(arr) == 0:
            return []
        arr = sorted(arr)
        arr = arr[::-1]
        arr = [to_w(i) for i in arr]
        return arr

    return by_length(arr)


print(by_length([2, 1, 1, 4, 5, 8, 2, 3]))
print(by_length([]))
print(by_length([1, -1, 55]))
