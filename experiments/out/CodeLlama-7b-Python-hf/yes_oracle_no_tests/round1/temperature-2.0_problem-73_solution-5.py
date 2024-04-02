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
    # Your code here
    #reversed_arr = arr[::-1]
    #reversed_arr = arr.reverse()
    #print(reversed_arr)

    #cnt = 0
    #for i in range(len(arr)):
    #    if arr[i] != reversed_arr[i]:
    #        cnt += 1
    #return cnt

    #return min(len(arr) - 2 * arr.count(arr[0]), len(arr) - 2 * arr.count(arr[-1]))

    #return min(len(arr) - 2 * arr.count(arr[0]), len(arr) - 2 * arr.count(arr[-1]), len(arr) - 2)

    #return min(len(arr) - arr.count(arr[0]), len(arr) - arr.count(arr[-1]))

    #return min(len(arr) - arr.count(arr[0]), len(arr) - arr.count(arr[-1]), len(arr) - 2)

    #return min(len(arr) - arr.count(arr[0]), len(arr) - arr.count(arr[-1]), len(arr) - 2)

    #return min(len(arr) - arr.count(arr[0]), len(arr) - arr.count(arr[-1]), len(arr) - 2)

    #return min(len(arr) - arr.count(arr[0]), len(arr) - arr.count(arr[-1]), len(arr) - 2)

    #return min(len(arr) - arr.count(arr[0]), len(arr) - arr.count(arr[-1]), len(arr) - 2)

    #return min(len(arr) - arr.count(arr[0]), len(arr) - arr.count(arr[-1]), len(arr) - 2)

    #return min(len(arr) - arr.count(arr[0]), len(arr) - arr.count(arr[-1]), len(arr) - 