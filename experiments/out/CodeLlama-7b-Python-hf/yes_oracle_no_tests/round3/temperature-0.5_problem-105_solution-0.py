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

    def to_w(n):
        if n == 1:
            return "One"
        elif n == 2:
            return "Two"
        elif n == 3:
            return "Three"
        elif n == 4:
            return "Four"
        elif n == 5:
            return "Five"
        elif n == 6:
            return "Six"
        elif n == 7:
            return "Seven"
        elif n == 8:
            return "Eight"
        elif n == 9:
            return "Nine"

    def reverse(arr):
        rev = []
        for i in reversed(arr):
            rev.append(i)
        return rev

    def sort(arr):
        arr.sort()
        return arr

    def filter(arr):
        for i in arr:
            if i < 1 or i > 9:
                arr.remove(i)
        return arr

    def to_str(arr):
        for i in range(len(arr)):
            arr[i] = to_w(arr[i])
        return arr

    arr = filter(arr)
    arr = sort(arr)
    arr = reverse(arr)
    arr = to_str(arr)

    return arr


print(by_length([2, 1, 1, 4, 5, 8, 2, 3]))
print(by_length([1, 1, 2, 2, 3, 4, 5, 8]))
print(by_length([1, 1, 2, 2, 3, 4, 5, 8, 10, 11, 12]))
print(by_length([]))
print(by_length([1, -1, 55]))
