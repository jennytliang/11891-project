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
    if not all(type(x) is int for x in arr):
        raise TypeError
    left, right, changes = 0, len(arr) - 1, 0
    while not isPal(arr): # if not Pal, swap
        while left == right or arr[left] == arr[right]:
            left += 1
            right -= 1
                    
        if left == right:
            left += 1
            right -= 1        
            
        arr[left], arr[right] = sorted(arr[left: right+1], reverse=not (left & 0b010)) # odd: reverse; eve: keep order       
        change += 2
    print(change)