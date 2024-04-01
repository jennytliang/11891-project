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
    """
    result = []
    sorted_list = sorted(filter(lambda x: 1 <= x <= 9, arr))
    for item in sorted_list[::-1]:
      result.append(to_word(item))
    return result
  
def to_word(number):
    """
    This is a private function called by the public function by_length. This function is only called
    if the numbers is between 1 and 9.
    return a string with a number from 1 to 9. 
    
    To handle negative numbers, convert the negative values to positive numbers and then reverse the
    resulting array. Then reverse the resulting string.
    
    For example, to_word(-1) will return 'Negative One'.
    """
    number_string = str(number)
    if number >= 0:
      return ' '.join(number_string.split()[::-1])
    else:
      number_string = str(-number)
      return number_string.split()
    