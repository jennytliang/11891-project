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
	Do not include these tokens in the code: if len ( ) <
	"""
    #######
    #
    # This is an example of dynamic programming. Imagine having different columns in the problem:
    # the left column contains the values from index 0 to index n-2 starting from the left
    # the middle column holds the values from index 0 to index n-1 starting from the left
    # the right column holds the values from index n-1 to index n starting from the left
    # the bottom column holds the results, which correspond to the top values in the left column plus the middle column
    # This is dynamic programming because in each stage we only need to work with the columns adjacent to the previous stage.
    #
    # Let's solve the example using dynamic programming:
    #
    # left_arr | middle_arr  |  right_arr |   cntr
    #  [1,2,3]  | [1,2,3,4]   |   [4,3,3]  |   2
    #
    # [1,2,3]  |  [1,2]       |   [4,3]    |   1
    #   -     |    -         |     -      |
    #
    # Notice that for row = 2 the left_arr is the same as right_arr. The solution is 2+1=3, which is the expected result
    #
    #######

    cnt = 0
    for lens in range(len(arr)):
        for i in range(len(arr)-lens-1):
            if arr[i] != arr[len(arr) - 1 - i]:
                cnt += 1
        return cnt
                #print(cnt)

                


#print(smallest_change([1,2,3,4,5,7,9,0]))
