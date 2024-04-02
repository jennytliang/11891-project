def smallest_change(arr):
    """
    Given an array arr of integers, find the minimum number of elements that
    need to be changed to make the array palindromic. A palindromic array is an array that
    is read the same backwards and forwards. In one change, you can change one element to any other element.

    For example:
    smallest_change([1,2,3,5,4,7,9,6]) == 4
    smallest_change([1, 2, 3, 4, 3, 2, 2]) == 1
    smallest_change([1, 2, 3, 2, 1]) == 0
    
	Do not include these tokens in the code: # first we need to make the
	"""
    # Write your code here.
    # We will use a nested loop to go through every element in the array
    # and keep track of the number of changes needed to make the array
    # palindromic.
    # We will use the counter variable to count the number of changes needed.
    # We will use a variable called current_element to keep track of the
    # current element in the array.
    # We will use a variable called previous_element to keep track of the
    # previous element in the array.
    # We will use a variable called is_palindromic to keep track of whether
    # the array is a palindromic.
    # We will use a variable called is_changing to keep track of whether the
    # current element is equal to the previous element.
    counter = 0
    current_element = 0
    previous_element = 0
    is_palindromic = True
    is_changing = False
    while is_palindromic:
        # We will use a nested loop to go through every element in the
        # array.
        for i in range(len(arr)):
            # We will check if the current element is equal to the previous
            # element.
            if current_element == previous_element:
                # We will increment the counter variable.
                counter += 1
                # We will set the is_changing variable to False.
                is_changing = False
            # We will check if the current element is not equal to the
            # previous element.
            elif current_element != previous_element and is_changing == False:
                # We will set the is_changing variable to True.
                is_changing = True
            # We will decrement the counter variable.
            counter -= 1
            # We will increment the current_element variable.
            current_element += 1
            # We will set the previous_element variable to the current
            # element.
            previous_element = current_element
            # We will check if the counter variable is equal to the length
            # of the array.
            if counter == len(arr):
                # We will set the is_pal