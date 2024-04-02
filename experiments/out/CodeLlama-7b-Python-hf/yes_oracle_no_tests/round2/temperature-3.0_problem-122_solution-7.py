def add_elements(arr, k):
    """
    Given a non-empty array of integers arr and an integer k, return
    the sum of the elements with at most two digits from the first k elements of arr.

    Example:

        Input: arr = [111,21,3,4000,5,6,7,8,9], k = 4
        Output: 24 # sum of 21 + 3

    Constraints:
        1. 1 <= len(arr) <= 100
        2. 1 <= k <= len(arr)
    
	Include these tokens in the code: def digits ( x : int ) -> int :
	"""
    # convert array to string
    arr = str(arr)
    # split the string
    split_arr = arr.split(",")
    # check each element in the array
    for i in range(len(split_arr)):
        # check if the element has more than 2 digits
        if len(split_arr[i]) > 2:
            # replace the element with the sum of the first 2 digits
            split_arr[i] = int(split_arr[i][0:2])
            # convert the array back to a string
            arr = str(split_arr)
            # replace the square brackets and quotations
            arr = arr.replace("[","")
            arr = arr.replace("]","")
            arr = arr.replace("'","")
            # convert the string back to a list
            arr = arr.split(",")
    # compute the sum
    sum = 0
    for i in range(len(arr)):
        sum += int(arr[i])
    return sum


# arr = [111,21,3,4000,5,6,7,8,9]
# k = 4
# print(add_elements(arr, k))

arr = [1,2,3,4,5,6,7,8,9,10]
k = 10
print(add_elements(arr, k))