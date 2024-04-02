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
    
	Do not include these tokens in the code: arr . sort () arr
	"""
    # first, we will first sort the array; we are going to use a bubble sort 
    length = len(arr)

    # create a "swap helper" function

    def swap(arr, i, j):
        temp = arr[i]
        arr[i] = arr[j]
        arr[j] = temp
    
    # begin to sort the arr with bubble sort
    for i in range(0, length):
        for j in range(i):

            # if the i value is less than the one to the left then swap
            if arr[i] < arr[j]:
                swap(arr, i, j)
    
    # now reverse the array/list       
    # to reverse the values of an array we will create a copy of arr and swap the elements in reverse

    rev_string = arr.copy()

    for i, item in enumerate(rev_string):
            swap(arr, i, (length - item) - 1)
    
    # now that the values are in the reverse we will use a dictionary to hold the values; 
    # then replace the values in the array.
    values = {
        1: "One",
        2: "Two",
        3: "Three",
        4: "Four",
        5: "Five",
        6: "Six",
        7: "Seven",
        8: "Eight",
        9: "Nine"

    }

    result = []
    # replace the values in the array with the corresponding name if it is between 1 and 9
    for item in arr:
        if 1 <= item <= 9:
            result.append("{}".format(values[item]))
        else:
            result.append(item)
    
    #return the result
    return result

print(by_length([2, 1, 1, 4, 5, 8, 2, 3]))