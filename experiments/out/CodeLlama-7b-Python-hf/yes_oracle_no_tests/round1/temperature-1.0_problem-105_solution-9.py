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
    
    newArray = []
    for i in arr:
        if (i >= 1 and i <= 9):
            newArray += [i]
    newArray.sort()
    while(len(newArray) > 0 and newArray[-1] == 9):
        newArray.pop()
    while(len(newArray) > 0 and newArray[0] == 1):
        newArray.pop(0)
    newArray = [x+1 for x in range(9) if x+1 not in newArray] + newArray

    finalArray = reversed(newArray)


    outputArray = []
    for i in finalArray:
        if (i == 1):
            outputArray += ["One"]
        if (i == 2):
            outputArray += ["Two"]
        if (i == 3):
            outputArray += ["Three"]
        if (i == 4):
            outputArray += ["Four"]
        if (i == 5):
            outputArray += ["Five"]
        if (i == 6):
            outputArray += ["Six"]
        if (i == 7):
            outputArray += ["Seven"]
        if (i == 8):
            outputArray += ["Eight"]
        if (i == 9):
            outputArray += ["Nine"]

    return outputArray

print(by_length([2, 1, 1, 4, 5, 8, 2, 3]))