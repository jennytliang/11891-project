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
    # Initialization
    sum_of_elements = 0
    max_two_digit_elements = []
    # Loop through array
    for i in range(len(arr)):
        # If element is less than 100, add to max_two_digit_elements
        if arr[i] < 100:
            max_two_digit_elements.append(arr[i])
        # If element is 100 or greater, loop through max_two_digit_elements
        else:
            for j in range(len(max_two_digit_elements)):
                # If the element is less than 100, add it to sum_of_elements
                if max_two_digit_elements[j] < 100:
                    sum_of_elements += max_two_digit_elements[j]
                # If the element is 100 or greater, pop the element
                elif max_two_digit_elements[j] >= 100:
                    max_two_digit_elements.pop(j)
                    break
    # Return sum of elements
    return sum_of_elements


# arr = [111,21,3,4000,5,6,7,8,9]
# k = 4
# print(add_elements(arr, k))

# arr = [100, 200, 1000, 10, 20]
# k = 2
# print(add_elements(arr, k))

arr = [1, 2, 3, 4, 5, 6]
k = 4
print(add_elements(arr, k))
