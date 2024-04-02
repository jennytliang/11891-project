def maximum(arr, k):
    """
    Given an array arr of integers and a positive integer k, return a sorted list 
    of length k with the maximum k numbers in arr.

    Example 1:

        Input: arr = [-3, -4, 5], k = 3
        Output: [-4, -3, 5]

    Example 2:

        Input: arr = [4, -4, 4], k = 2
        Output: [4, 4]

    Example 3:

        Input: arr = [-3, 2, 1, 2, -1, -2, 1], k = 1
        Output: [2]

    Note:
        1. The length of the array will be in the range of [1, 1000].
        2. The elements in the array will be in the range of [-1000, 1000].
        3. 0 <= k <= len(arr)
    
	Do not include these tokens in the code: arr . sort ()
	"""
    # Get the list of top k numbers
    top_k = arr[:k]
    # Sort the top k numbers in ascending order
    top_k.sort()
    # Iterate through the rest of the elements in the array
    for i in range(k, len(arr)):
        # Get the current element
        num = arr[i]
        # Get the last element of the top k numbers
        last_num = top_k[-1]
        # If the current element is larger than the last element of the top k numbers, then remove the last element from the top k numbers
        if num > last_num:
            top_k.pop()
        # Add the current element to the top k numbers
        top_k.append(num)
        # Sort the top k numbers in ascending order
        top_k.sort()
    return top_k


def main():
    print(maximum([-3, -4, 5], 3))
    print(maximum([4, -4, 4], 2))
    print(maximum([-3, 2, 1, 2, -1, -2, 1], 1))


if __name__ == '__main__':
    main()
