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

    arr_sorted = [str(elements) for elements in arr]

    arr_sorted.sort(key=lambda x: len(str(x)))
    result = sum(arr_sorted[:k])
    ##print (result)
    return result 

if __name__ == "__main__": 
    arr = [111,21,3,1,4000,5,1,6,3,10,9] 
    k = 4
    print (add_elements(arr, k))
    ##test.assert_equals(add_elements(arr, k), 45)