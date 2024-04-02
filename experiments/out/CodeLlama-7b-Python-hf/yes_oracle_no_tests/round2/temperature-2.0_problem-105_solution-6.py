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

    def to_w(number):
        if number == 1:
            return "One"
        if number == 2:
            return "Two"
        if number == 3:
            return "Three"
        if number == 4:
            return "Four"
        if number == 5:
            return "Five"
        if number == 6:
            return "Six"
        if number == 7:
            return "Seven"
        if number == 8:
            return "Eight"
        if number == 9:
            return "Nine"

    def by_length(arr):
        arr.sort()
        arr.reverse()
        for i in range(len(arr)):
            if arr[i] >= 1 and arr[i] <= 9:
                arr[i] = to_w(arr[i])
            else:
                arr[i] = str(arr[i])
        return arr

    return by_length(arr)


# print(by_length([2, 1, 1, 4, 5, 8, 2, 3]))
# print(by_length([]))
# print(by_length([1, -1 , 55]))
