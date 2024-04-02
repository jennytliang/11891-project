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


    def to_digit_dict(arr, num):
        """ 
        Given an array of integers and a number int, count the times a digit appears in the array.
        Return the number of appearances in its corresponding position in a dictionary where the
        key is the number and the value is its count.
        Ex:
          arr = [1, 2, 1, 4, 5, 8]
          num = 5              
          1 appeared in 2 times
          2 appeared in 1 time
          4 and 8 did not appear once
          5 appeared in 1 time
          -> {1: 2, 2: 1, 5: 1)
        """
        digits = {i + 1: 0 for i in range(9)}
        for num in arr:
            if 1 <= num <= 9:
                digits[num] += 1
        return digits


    def digit_to_name(num_digit):
        if num_digit == 1:
            return "One"
        elif num_digit == 2:
            return "Two"
        elif num_digit == 3:
            return "Three"
        elif num_digit == 4:
            return "Four"
        elif num_digit == 5:
            return "Five"
        elif num_digit == 6:
            return "Six"
        elif num_digit == 7:
            return "Seven"
        elif num_digit == 8:
            return "Eight"
        elif num_digit == 9:
            return "Nine"
        return ""


    if not arr:
        return []
    arr.sort()
    arr.reverse()
    digits = to_digit_dict(arr, arr[0])

    output = list(range(1, 10)) # start from one because arr starts from one
    count, i = 0, 0

    # fill count and i with their corresponding digit.
    while True:
        if digits.get(count + 1) and digits[count + 1] != 0: # check if digit exist
            i += digits