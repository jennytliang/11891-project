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
    # Step 1: Sort the array in ascending order
    arr.sort()
    # Step 2: Reverse the array
    arr.reverse()
    # Step 3: Create a list to store the output
    result = []
    # Step 4: Iterate through the sorted array
    for num in arr:
        # If the number is a digit between 1 and 9, map it to its name
        if 1 <= num <= 9:
            result.append(to_word(num))
        # Otherwise, append the number to the result
        else:
            result.append(num)
    return result


def to_word(num):
    """
    Convert a number to its name
    """
    if num == 1:
        return "One"
    if num == 2:
        return "Two"
    if num == 3:
        return "Three"
    if num == 4:
        return "Four"
    if num == 5:
        return "Five"
    if num == 6:
        return "Six"
    if num == 7:
        return "Seven"
    if num == 8:
        return "Eight"
    if num == 9:
        return "Nine"


def test_by_length():
    assert by_length([]) == []
    assert by_length([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == ["One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten"]
    assert by_length([5, 2, 3, 4, 1, 6, 7, 8, 9, 10]) == ["Five", "Two", "Three", "Four", "One", "Six", "Seven", "Eight", "Nine", "Ten"]
    assert by_length([1, 2, 3, 4, 5, 6, 7, 