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
                
    
	Include these tokens in the code: sorted _ arr
	Do not include these tokens in the code: # 1 st solution
	"""
    # Your code goes here
    # first solution
    # return sorted(arr) == arr

    # second solution
    # return arr == sorted(arr) or arr == sorted(arr, reverse=True)

    # third solution
    # if len(arr) == 0:
    #     return True
    # if arr[-1] > arr[0]:
    #     return False
    # for i in range(1, len(arr)):
    #     if arr[i - 1] > arr[i]:
    #         return False
    # return True

    # fourth solution
    # n = len(arr)
    # for i in range(n - 1):
    #     if arr[i] > arr[i + 1]:
    #         return False
    # return True

    # fifth solution
    # return arr == sorted(arr) or arr == sorted(arr, reverse=True)

    # sixth solution
    # return arr == sorted(arr) or arr == sorted(arr, reverse=True)

    # seventh solution
    # return arr == sorted(arr) or arr == sorted(arr, reverse=True)

    # eighth solution
    # return arr == sorted(arr) or arr == sorted(arr, reverse=True)

    # ninth solution
    # return arr == sorted(arr) or arr == sorted(arr, reverse=True)

    # tenth solution
    # return arr == sorted(arr) or arr == sorted(arr, reverse=True)

    # eleventh solution
    # return arr == sorted(arr) or arr == sorted(arr, reverse=True)

    # twelfth solution
    # return arr == sorted(arr) or arr == sorted(arr, reverse=True)

    # thirteenth solution
    # return arr == sorted(arr) or arr == sorted(arr, reverse=True)

    # fourteenth solution
    # return arr == sorted(arr) or arr == sorted(arr, reverse=True)

    # fifteenth solution
    # return arr == sorted(arr) or arr == sorted(arr, reverse=True)

