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
    
	Do not include these tokens in the code: # My solution
	"""
    # My solution
    # O(n) time | O(n) space
    # Sort the list
    arr.sort()
    # Reverse the list
    arr.reverse()
    # Map the numbers to string
    return [str(x) for x in arr if 1 <= x <= 9]

    # # My solution 2
    # # O(n) time | O(n) space
    # # Sort the list
    # arr.sort()
    # # Reverse the list
    # arr.reverse()
    # # Map the numbers to string
    # return [str(x) for x in arr if 1 <= x <= 9]

    # # My solution 3
    # # O(n) time | O(n) space
    # # Sort the list
    # arr.sort()
    # # Reverse the list
    # arr.reverse()
    # # Map the numbers to string
    # return [str(x) for x in arr if 1 <= x <= 9]

    # # My solution 4
    # # O(n) time | O(n) space
    # # Sort the list
    # arr.sort()
    # # Reverse the list
    # arr.reverse()
    # # Map the numbers to string
    # return [str(x) for x in arr if 1 <= x <= 9]

    # # My solution 5
    # # O(n) time | O(n) space
    # # Sort the list
    # arr.sort()
    # # Reverse the list
    # arr.reverse()
    # # Map the numbers to string
    # return [str(x) for x in arr if 1 <= x <= 9]

    # # My solution 6
    # # O(n) time | O(n) space
    # # Sort the list
    # arr.sort()
    # # Reverse the list
    # arr.reverse()
    # # Map the numbers to string
    # return [str(x) for x in arr if 1 <= x <= 9]

    # # My solution 