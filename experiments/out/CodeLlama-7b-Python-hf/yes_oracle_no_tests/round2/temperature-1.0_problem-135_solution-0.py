def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    
	Include these tokens in the code: for i in range ( len ( arr ) -
	"""

    # Get the maximum and create a dict for storing indices
    largest = largest=max(arr)
    index = {}

    # Create a dict with indices
    for i in range(len(arr)-1):
        index[arr[i]] = i
    
    # Traverse the array from end to beginning and find which element can be put in index of i
    for i in range(len(arr)-1,0,-1):
        if arr[i] <= (largest - arr[i]+1):
            if index.get(arr[i] + arr[i - 1]-1) is not None:
                return index[arr[i] + arr[i - 1]-1]

    return -1
        

test_data = [
    [1,2,4,3,5],
    [1,2,3],
    [5,4,3,2,1],
    [2, 1],
    [5, 1, 3, 2, 4],
    [5,3,1]
]

expected_output = [
    3,
    -1,
    0,
    -1,
    3,
    0
]

final_output = []

for idx, data in enumerate(test_data):
    final_output.append(can_arrange(data))

# Do not change anything here. We have defined a function called assert_equal
# which is already implemented and is a faster way to run and test your code.
assert_equal(final_output, expected_output)
