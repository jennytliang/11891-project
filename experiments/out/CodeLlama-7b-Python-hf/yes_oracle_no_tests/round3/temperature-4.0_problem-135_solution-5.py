def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    
	Do not include these tokens in the code: # Your code here
	"""
    # TODO: Remove this comment when you've written your code
    #raise NotImplementedError()
    # TODO: Write your code here
    #raise NotImplementedError()
    
    def can_arrange(arr):
		"""Create a function which returns the largest index of an element which
		is not greater than or equal to the element immediately preceding it. If
		no such element exists then return -1. The given array will not contain
		duplicate values.

		Examples:
		can_arrange([1,2,4,3,5]) = 3
		can_arrange([1,2,3]) = -1
		"""
		# TODO: Remove this comment when you've written your code
		#raise NotImplementedError()
		# TODO: Write your code here
		#raise NotImplementedError()
		
		for i in range(len(arr)):
			if arr[i] <= arr[i-1]:
				return i-1
		return -1


    return can_arrange(arr)
