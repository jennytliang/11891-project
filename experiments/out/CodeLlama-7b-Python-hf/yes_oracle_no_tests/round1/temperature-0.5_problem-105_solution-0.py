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

    # Sort the array
    arr.sort()

    # Create an empty string to store the results
    result = ""

    # For each item in the array
    for item in arr:
        # If the item is between 1 and 9 inclusive
        if 1 <= item <= 9:
            # Add the word to the result string
            result += to_word(item) + " "
        
        # Else if the item is 10
        elif item == 10:
            # Add "Ten" to the result string
            result += "Ten "

        # Else if the item is 11
        elif item == 11:
            # Add "Eleven" to the result string
            result += "Eleven "

        # Else if the item is 12
        elif item == 12:
            # Add "Twelve" to the result string
            result += "Twelve "

        # Else if the item is 13
        elif item == 13:
            # Add "Thirteen" to the result string
            result += "Thirteen "

        # Else if the item is 14
        elif item == 14:
            # Add "Fourteen" to the result string
            result += "Fourteen "

        # Else if the item is 15
        elif item == 15:
            # Add "Fifteen" to the result string
            result += "Fifteen "

        # Else if the item is 16
        elif item == 16:
            # Add "Sixteen" to the result string
            result += "Sixteen "

        # Else if the item is 17
        elif item == 17:
            # Add "Seventeen" to the result string
            result += "Seventeen "

        # Else if the item is 18
        elif item == 18:
            # Add "Eighteen" to the result string
            result += "Eighteen "

        # Else if the item is 19
        elif item == 19:
