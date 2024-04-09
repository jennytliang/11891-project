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
    
	Include these tokens in the code: x : int ) -> str :
	Do not include these tokens in the code: num ):
	"""


    def to_name(x):
        if x == 1: return "One"
        if x == 2: return "Two"
        if x == 3: return "Three"
        if x == 4: return "Four"
        if x == 5: return "Five"
        if x == 6: return "Six"
        if x == 7: return "Seven"
        if x == 8: return "Eight"
        if x == 9: return "Nine"

    def to_string(x):
        if x == 1: return "One"
        if x == 2: return "Two"
        if x == 3: return "Three"
        if x == 4: return "Four"
        if x == 5: return "Five"
        if x == 6: return "Six"
        if x == 7: return "Seven"
        if x == 8: return "Eight"
        if x == 9: return "Nine"

    def sort_array(arr):
        arr.sort()
        return arr

    def reverse_array(arr):
        arr.reverse()
        return arr

    def reverse_string(x):
        return x[::-1]

    def remove_string(x):
        return x[1:]

    def by_length(arr):
        result = []
        for i in arr:
            if i < 10 and i > 0:
                result.append(to_name(i))
        result.sort()
        result = reverse_string(result)
        result = [remove_string(i) for i in result]
        return result

    def to_string(arr):
        result = []
        for i in arr:
            result.append(to_name(i))
        return result

    def by_length(arr):
        result = []
        for i in arr:
            if i < 10 and i > 0:
                result.append(to_name(i))
        result.sort()
        result = reverse