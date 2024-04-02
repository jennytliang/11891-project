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
    
	Do not include these tokens in the code: # by _ length ( [ 2
	"""
    def by_length(arr):
        if len(arr) == 0:
            return []
        else:
            arr.sort()
            arr.reverse()
            for i in range(len(arr)):
                if arr[i] >= 1 and arr[i] <= 9:
                    arr[i] = str(arr[i])
                    if arr[i] == "1":
                        arr[i] = "One"
                    elif arr[i] == "2":
                        arr[i] = "Two"
                    elif arr[i] == "3":
                        arr[i] = "Three"
                    elif arr[i] == "4":
                        arr[i] = "Four"
                    elif arr[i] == "5":
                        arr[i] = "Five"
                    elif arr[i] == "6":
                        arr[i] = "Six"
                    elif arr[i] == "7":
                        arr[i] = "Seven"
                    elif arr[i] == "8":
                        arr[i] = "Eight"
                    elif arr[i] == "9":
                        arr[i] = "Nine"
                else:
                    arr[i] = "One"
            return arr
    print(by_length([2, 1, 1, 4, 5, 8, 2, 3]))
    print(by_length([]))
    print(by_length([1, -1, 55]))
    print(by_length([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))


# 2. Counting Duplicates

def count_duplicates(arr):
    """
    Given an array of integers, return the number of integers in the array that appear more than once.
    
    For example:
      arr = [3, 1, 3, 2, 2, 1, 3, 3]
      return 4
    