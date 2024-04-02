def move_one_ball(arr):
    """We have an array 'arr' of N integers arr[1], arr[2], ..., arr[N].The
    numbers in the array will be randomly ordered. Your task is to determine if
    it is possible to get an array sorted in non-decreasing order by performing 
    the following operation on the given array:
        You are allowed to perform right shift operation any number of times.
    
    One right shift operation means shifting all elements of the array by one
    position in the right direction. The last element of the array will be moved to
    the starting position in the array i.e. 0th index. 

    If it is possible to obtain the sorted array by performing the above operation
    then return True else return False.
    If the given array is empty then return True.

    Note: The given list is guaranteed to have unique elements.

    For Example:
    
    move_one_ball([3, 4, 5, 1, 2])==>True
    Explanation: By performin 2 right shift operations, non-decreasing order can
                 be achieved for the given array.
    move_one_ball([3, 5, 4, 1, 2])==>False
    Explanation:It is not possible to get non-decreasing order for the given
                array by performing any number of right shift operations.
                
    
	Do not include these tokens in the code: arr . sort () size
	"""
    # If the given array is empty then return True
    if not arr:
        return True

    # If the given array is of size 1 then return True
    if len(arr) == 1:
        return True

    # If the given array is of size 2 then return True if the given array is
    # sorted else return False
    if len(arr) == 2:
        return arr[0] <= arr[1]

    # If the given array is of size 3 then return True if the given array is
    # sorted else return False
    if len(arr) == 3:
        return arr[0] <= arr[1] <= arr[2]

    # If the given array is of size 4 then return True if the given array is
    # sorted else return False
    if len(arr) == 4:
        return arr[0] <= arr[1] <= arr[2] <= arr[3]

    # If the given array is of size 5 then return True if the given array is
    # sorted else return False
    if len(arr) == 5:
        return arr[0] <= arr[1] <= arr[2] <= arr[3] <= arr[4]

    # If the given array is of size 6 then return True if the given array is
    # sorted else return False
    if len(arr) == 6:
        return arr[0] <= arr[1] <= arr[2] <= arr[3] <= arr[4] <= arr[5]

    # Sort the given array
    arr.sort()

    # If the given array is of size 7 then return True if the given array is
    # sorted else return False
    if len(arr) == 7:
        return arr[0] <= arr[1] <= arr[2] <= arr[3] <= arr[4] <= arr[5] <= arr[6]

    # If the given array is of size 8 then return True if the given array is
    # sorted else return False
    if len(arr) == 8:
        return (
            arr[0] <= arr[1