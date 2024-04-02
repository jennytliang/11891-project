def prod_signs(arr):
    """
    You are given an array arr of integers and you need to return
    sum of magnitudes of integers multiplied by product of all signs
    of each number in the array, represented by 1, -1 or 0.
    Note: return None for empty arr.

    Example:
    >>> prod_signs([1, 2, 2, -4]) == -9
    >>> prod_signs([0, 1]) == 0
    >>> prod_signs([]) == None
    
	Include these tokens in the code: arr
	Do not include these tokens in the code: len ( )
	"""

  #code goes here

if __name__ == '__main__':
    # Test your code with this first
    # Change the argument to try different values
    print("Pass" if prod_signs([1, 2, 2, -4]) == -9 else "Fail")

    # After you are satisfied with your results, use input() to prompt the user for a string array
    #arr = input("Input numbers separated by spaces: ").split()
    # Print the sum of magnitudes of integers multiplied by product of all signs of each number in the array
    #print(prod_signs(arr))
