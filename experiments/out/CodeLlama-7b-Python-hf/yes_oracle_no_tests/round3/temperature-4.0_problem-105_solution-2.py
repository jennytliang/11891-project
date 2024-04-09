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
    
	Include these tokens in the code: def to _ word ( x : int ) ->
	"""
    # 1st line: reverse the array
    # 2nd line: iterate and sort the elements
    # 3rd line: iterate and return the elements
    # 4th line: if the array is empty return an empty array
    # 5th line: if the array has any strange number ignore it
    # 6th line: return the elements
    # Write your code below this line
    arr.reverse()
    arr.sort()
    ret_arr = []
    if len(arr) == 0:
        return []
    for i in range(len(arr)):
        if arr[i] >= 1 and arr[i] <= 9:
            ret_arr.append(to_word(arr[i]))
        else:
            ret_arr.append(arr[i])
    return ret_arr

def to_word(num):
    if num == 1:
        return 'One'
    elif num == 2:
        return 'Two'
    elif num == 3:
        return 'Three'
    elif num == 4:
        return 'Four'
    elif num == 5:
        return 'Five'
    elif num == 6:
        return 'Six'
    elif num == 7:
        return 'Seven'
    elif num == 8:
        return 'Eight'
    elif num == 9:
        return 'Nine'
    else:
        return num

print(by_length([2, 1, 1, 4, 5, 8, 2, 3]))
print(by_length([]))
print(by_length([1, -1 , 55]))
