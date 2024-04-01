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
    
	Include these tokens in the code:  def to _ word ( x : int
	"""

    # 1) sort the array
    # 2) reverse the array
    # 3) for each digit, map it to the word
    # 4) return the list of words

    # 1) sort the array
    arr.sort()

    # 2) reverse the array
    arr.reverse()

    # 3) for each digit, map it to the word
    words = []
    for digit in arr:
        if digit == 1:
            words.append("One")
        elif digit == 2:
            words.append("Two")
        elif digit == 3:
            words.append("Three")
        elif digit == 4:
            words.append("Four")
        elif digit == 5:
            words.append("Five")
        elif digit == 6:
            words.append("Six")
        elif digit == 7:
            words.append("Seven")
        elif digit == 8:
            words.append("Eight")
        elif digit == 9:
            words.append("Nine")

    # 4) return the list of words
    return words

print(by_length([2, 1, 1, 4, 5, 8, 2, 3]))
print(by_length([]))
print(by_length([1, -1 , 55]))
