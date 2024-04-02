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
    # ... code
    result = []

    for num in sorted(arr):
        if 1 <= num <= 9:
            string = "One" if num == 1 else "Two" if num == 2 else "Three" if num == 3 else "Four" \
                    if num == 4 else "Five" if num == 5 else "Six" if num == 6 else "Seven" \
                     if num == 7 else "Eight" if num == 8 else "Nine"
            digit = string[0]
            result.append(digit)

    result.reverse()
    for index in range(len(result)):
        if result[index] == "i":
            result[index] = "One"
        if result[index] == "o":
            result[index] = "O"
        digit = int(result[index]) + 1
        result[index] = "Zero" if digit == 0 else "One" if digit == 1 else "Two" \
                        if digit == 2 else "Three" if digit == 3 else "Four" \
                        if digit == 4 else "Five" if digit == 5 else "Six" \
                         if digit == 6 else "Seven" if digit == 7 else "Eight" \
                          if digit == 8 else "Nine"

    for index in range(len(result)):
        if result[index] == "One":
            result[index] = "First"
        if result[index] == "Two":
            result[index] = "Second"
        if result[index] == "Three":
            result[index] = "Third"
        if result[index] == "Four":
            result[index] = "Fourth"
        if result[index] == "Five":
            result[index] = "Fifth"
        if result[index] == "Six":
            result[index] = "Sixth"
        if result[index] == "Seven":
            result[index] = "Seventh"
        if