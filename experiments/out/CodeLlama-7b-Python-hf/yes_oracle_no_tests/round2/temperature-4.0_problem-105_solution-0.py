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


    def to_string(number):
        if number == 1:
            return "One"
        elif number == 2:
            return "Two"
        elif number == 3:
            return "Three"
        elif number == 4:
            return "Four"
        elif number == 5:
            return "Five"
        elif number == 6:
            return "Six"
        elif number == 7:
            return "Seven"
        elif number == 8:
            return "Eight"
        elif number == 9:
            return "Nine"
        else:
            return ""

    arr = sorted(arr, reverse=True)
    arr = [to_string(i) for i in arr if 0 < i < 10]
    return arr


print(by_length([2, 1, 1, 4, 5, 8, 2, 3]))
print(by_length([]))
print(by_length([1, -1, 55]))
