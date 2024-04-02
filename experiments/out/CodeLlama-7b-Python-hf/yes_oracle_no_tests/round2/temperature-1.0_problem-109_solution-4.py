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
	Do not include these tokens in the code: N
	"""
    n = len(arr)
    if n==0: return True
    # The following array stores the current position of the numbers.
    # For example
    # curr_arr=[0, 1, 2, 3, 4]  i.e., number 1 is in arr[1], ..., number 2 is in arr[2] ...
    curr_arr=np.arange(n) 
    # Initialize the array to the number of swaps for initial order.
    swaps = n-1 
    
    arr_ = arr.copy()
    if arr.min()==arr[0] or arr.max()==arr[n-1]:
        return False
    
    j=0 # j will maintain the index of the element that is to be swapped
    for i in range(n):
        
        # As the right most number is the greatest number
        if arr[i]==arr[n-1]:
            for a in range(n-1):
                if arr_[a]>arr[a].max():  # If the next min value is greater
                    arr_ = np.roll(arr_, -1)  # Then swap all to right
                    swaps+=1
                    arr_[n-1]=arr[i]
                    break
            else:
                # Here, number is already in its place, Hence one more left shift
                # will be reqd. We store one less left shift
                # in swaps because right shift does not count as 
                # one more left shift to be done.
                swaps-=1
        else:
            arr_ = np.roll(arr_, -1)
            swaps+=1
            arr_[n-1]=arr[i]
        # For each of the i number of swaps, we compute the 
        # position of element to be swapped as the difference
        # between current position of the element and actual 
        # position of the element in arr_
        j=np.abs(arr_[i] - curr_arr[i]).argmax() 
        swap_val = curr_arr[i]
        swap_j = curr