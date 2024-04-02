def smallest_change(arr):
    """
    Given an array arr of integers, find the minimum number of elements that
    need to be changed to make the array palindromic. A palindromic array is an array that
    is read the same backwards and forwards. In one change, you can change one element to any other element.

    For example:
    smallest_change([1,2,3,5,4,7,9,6]) == 4
    smallest_change([1, 2, 3, 4, 3, 2, 2]) == 1
    smallest_change([1, 2, 3, 2, 1]) == 0
    
	Include these tokens in the code: arr _ re vers ed , c nt = arr
	"""

    # Create copies of the original array for use
    re_arr = list(arr)
    cnt_arr = list(arr)
    for idx, elem in enumerate(cnt_arr):
        if elem < idx < len(cnt_arr) - 1:
            cnt_arr[idx] = -1
        elif elem > idx and elem<len(arr):
            cnt_arr[idx] = -1
        else: cnt_arr[idx] = 0
    
    # Make arr = arr and cnt= (1,2,2,1) using while loop
    # Continue iterating the loop while 0s are still in cnt
    # If there is already a 0 in a certain index, stop iterating
    while 0 in cnt_arr:
        # Iterate over arr
        for i, a in enumerate(arr):
            # If arr[i] = index AND a is in bounds
            if a > i and a<len(arr):
                # Get the value corresponding with index
                check_val = re_arr[a]
                # If the value corresponds with index, check if it is within the bounds of arr or arr[i-1]
                if check_val == i:
                    # If it is, decrease counter by 1
                    cnt_arr[i] += -1
                elif check_val <= i - 1:
                    # else change the corresponding value in cnt_arr
                    cnt_arr[i] += 1
            # If arr[i] is less than i
            else:
                # Decrease count by 1
                cnt_arr[i] = 1
    
    return (max(cnt_arr)+len(arr)) - len(arr)

def smallest_change_efficent(arr):
    # Get the length of the array
    n = len(arr)
    # Calculate the total count with 2n - sum(arr)
    count = 2*n - sum(arr)
    # Iterate over arr and calculate the number of zeros
    for i, a in enumerate(arr):
        # If the