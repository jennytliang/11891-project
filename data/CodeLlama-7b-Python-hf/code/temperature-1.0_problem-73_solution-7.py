def smallest_change(arr):
    """
    Given an array arr of integers, find the minimum number of elements that
    need to be changed to make the array palindromic. A palindromic array is an array that
    is read the same backwards and forwards. In one change, you can change one element to any other element.

    For example:
    smallest_change([1,2,3,5,4,7,9,6]) == 4
    smallest_change([1, 2, 3, 4, 3, 2, 2]) == 1
    smallest_change([1, 2, 3, 2, 1]) == 0
    """
    if len(arr) < 2:
        return 0
    if len(arr) == 2:
        if arr[0] == arr[1]:
            return 0
        else:
            return 1
    if len(arr) == 3:
        if arr[0] == arr[2]:
            return 1
        elif arr[0] == arr[1]:
            return 1
        elif arr[1] == arr[2]:
            return 1
        else:
            return 2
    if len(arr) == 4:
        if arr[0] == arr[3]:
            return 2
        elif arr[0] == arr[2]:
            return 2
        elif arr[1] == arr[3]:
            return 2
        elif arr[1] == arr[2]:
            return 2
        else:
            return 3
    if len(arr) == 5:
        if arr[0] == arr[4]:
            return 3
        elif arr[0] == arr[3]:
            return 3
        elif arr[1] == arr[4]:
            return 3
        elif arr[1] == arr[3]:
            return 3
        elif arr[2] == arr[4]:
            return 3
        elif arr[2] == arr[3]:
            return 3
        else:
            return 4
    if len(arr) == 6:
        if arr[0] == arr[5]:
            return 4
        elif arr[0] == arr[4]:
            return 4
        elif arr[0] == arr[3]:
            return 4
        elif arr[0] == arr[2]:
            return 4
        elif arr[1] == arr[5]:
            return 4
        elif arr[1] == arr[4]:
            return 4
        elif arr[1] == arr[3]:
            return 4
        elif arr[1] == arr[2]:
            return 4
        elif arr[2] == arr[5]:
            return 4
        elif arr[2] == arr[4]:
            return 4
        elif arr[2] == arr[3]:
            return 4
        elif arr[3] == arr[5]:
            return 4
        elif arr[3] == arr[4]:
            return 4
        else:
            return 5
    if len(arr) == 7:
        if arr[0] == arr[6]:
            return 5
        elif arr[0] == arr[5]:
            return 5
        elif arr[0] == arr[4]:
            return 5
        elif arr[0] == arr[3]:
            return 5
        elif arr[0] == arr[2]:
            return 5
        elif arr[1] == arr[6]:
            return 5
        elif arr[1] == arr[5]:
            return 5
        elif arr[1] == arr[4]:
            return 5
        elif arr[1] == arr[3]:
            return 5
        elif arr[1] == arr[2]:
            return 5
        elif arr[2] == arr[6]:
            return 5
        elif arr[2] == arr[5]:
            return 5
        elif arr[2] == arr[4]:
            return 5
        elif arr[2] == arr[3]:
            return 5
        elif arr[3] == arr[6]:
            return 5
        elif arr[3] == arr[5]:
            return 5
        elif arr[3] == arr[4]:
            return 5
        elif arr[4] == arr[6]:
            return 5
        elif arr[4] == arr[5]:
            return 5
        else:
            return 6
    if len(arr) == 8:
        if arr[0] == arr[7]:
            return 6
        elif arr[0] == arr[6]:
            return 6
        elif arr[0] == arr[5]:
            return 6
        elif arr[0] == arr[4]:
            return 6
        elif arr