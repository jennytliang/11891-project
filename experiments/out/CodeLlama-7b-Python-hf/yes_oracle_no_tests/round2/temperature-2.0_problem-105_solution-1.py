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
    
	Include these tokens in the code: def to
	Do not include these tokens in the code: return [
	"""
    # 1. Sort the array
    arr.sort()
    # 2. Reverse the array
    arr.reverse()
    # 3. Create a list of strings
    arr_str = []
    # 4. Loop through the array and convert the numbers to strings
    for i in arr:
        if i >= 1 and i <= 9:
            arr_str.append(str(i))
    # 5. Loop through the array and convert the strings to names
    for i in range(len(arr_str)):
        if arr_str[i] == "1":
            arr_str[i] = "One"
        elif arr_str[i] == "2":
            arr_str[i] = "Two"
        elif arr_str[i] == "3":
            arr_str[i] = "Three"
        elif arr_str[i] == "4":
            arr_str[i] = "Four"
        elif arr_str[i] == "5":
            arr_str[i] = "Five"
        elif arr_str[i] == "6":
            arr_str[i] = "Six"
        elif arr_str[i] == "7":
            arr_str[i] = "Seven"
        elif arr_str[i] == "8":
            arr_str[i] = "Eight"
        elif arr_str[i] == "9":
            arr_str[i] = "Nine"
    # 6. Return the list of strings
    return arr_str


print(by_length([2, 1, 1, 4, 5, 8, 2, 3]))
print(by_length([2, 1, 1, 4, 5, 8, 2, 3, 2, 1, 1, 4, 5, 8, 2, 3]))
print(by_length([]))
print(by_length([1, -1, 55]))
print(by_length([1, -1, 55,