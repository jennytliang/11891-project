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
                
    
	Include these tokens in the code: sorted _ arr = sorted ( arr )
	Do not include these tokens in the code: # Your code goes here
	"""
    if len(arr) == 0:
        return True
    arr = sorted(arr)
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            return False
    return True


def test_function(test_case):
    arr = test_case[0]
    solution = test_case[1]
    output = move_one_ball(arr)
    if output == solution:
        print("Pass")
    else:
        print("Fail")


arr = [3, 4, 5, 1, 2]
solution = True
test_case = [arr, solution]
test_function(test_case)

arr = [3, 5, 4, 1, 2]
solution = False
test_case = [arr, solution]
test_function(test_case)

arr = [1, 2, 3, 4, 5]
solution = True
test_case = [arr, solution]
test_function(test_case)

arr = []
solution = True
test_case = [arr, solution]
test_function(test_case)

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
solution = True
test_case = [arr, solution]
test_function(test_case)

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21]
solution = False
test_case = [arr, solution]
test_function(test_case)
