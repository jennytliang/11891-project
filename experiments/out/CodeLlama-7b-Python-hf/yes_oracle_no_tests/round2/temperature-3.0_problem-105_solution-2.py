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
    
	Include these tokens in the code: : int ) -> str : if x
	Do not include these tokens in the code: ):
	"""

    def to_w(x):
        if x == 1:
            return "One"
        elif x == 2:
            return "Two"
        elif x == 3:
            return "Three"
        elif x == 4:
            return "Four"
        elif x == 5:
            return "Five"
        elif x == 6:
            return "Six"
        elif x == 7:
            return "Seven"
        elif x == 8:
            return "Eight"
        elif x == 9:
            return "Nine"
        else:
            return ""

    def reverse(arr):
        new_arr = []
        for i in range(len(arr) - 1, -1, -1):
            new_arr.append(arr[i])
        return new_arr

    def sort(arr):
        new_arr = []
        for i in range(1, 10):
            for j in range(len(arr)):
                if arr[j] == i:
                    new_arr.append(i)
        return new_arr

    arr = sort(arr)
    arr = reverse(arr)
    new_arr = []
    for i in range(len(arr)):
        new_arr.append(to_w(arr[i]))
    return new_arr


print(by_length([2, 1, 1, 4, 5, 8, 2, 3]))
print(by_length([]))
print(by_length([1, -1, 55]))
