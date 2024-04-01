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
    
    diff_pal, n = 0, len(arr)
    
    mid_indx =  len(arr) // 2
    left_half, right_half = arr[0:mid-indx], arr[mid-indx+1, -1]  # splits into left, right halves
    temp_lh, temp_rh = left_half.copy(), reversed(list.copy(re.right)
                      


for i  in (range(1,n-i+1) : 
      