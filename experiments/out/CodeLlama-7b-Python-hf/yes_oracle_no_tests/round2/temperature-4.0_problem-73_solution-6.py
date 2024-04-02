def smallest_change(arr):
    """
    Given an array arr of integers, find the minimum number of elements that
    need to be changed to make the array palindromic. A palindromic array is an array that
    is read the same backwards and forwards. In one change, you can change one element to any other element.

    For example:
    smallest_change([1,2,3,5,4,7,9,6]) == 4
    smallest_change([1, 2, 3, 4, 3, 2, 2]) == 1
    smallest_change([1, 2, 3, 2, 1]) == 0
    
	Include these tokens in the code: arr _ re vers ed ,
	Do not include these tokens in the code: = []
	"""
    # TODO: Write your solution here
    # for i in range(len(arr)):
    #     for j in range(i+1, len(arr)):
    #         if arr[i]!=arr[j]:
    #             arr[j]=arr[i]
    #             return arr
    # return arr
    # print(arr)
    # i=0
    # while i<len(arr):
    #     j=len(arr)-1
    #     while i<j:
    #         if arr[i]!=arr[j]:
    #             arr[i]=arr[j]
    #             arr[j]=arr[i]
    #             # print(arr)
    #             return arr
    #         j-=1
    #     i+=1
    # return arr
    # print(arr)
    i=0
    while i<len(arr):
        j=len(arr)-1
        while i<j:
            if arr[i]!=arr[j]:
                arr[i]=arr[j]
                arr[j]=arr[i]
                # print(arr)
                return arr
            j-=1
        i+=1
    return arr


"""
arr = [1, 2, 3, 2, 1]
arr = [1, 2, 3, 5, 4, 7, 9, 6]
arr = [1, 2, 3, 4, 3, 2, 2]
print(smallest_change(arr))
"""
