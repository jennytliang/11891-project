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

    # initialize variables
    total = 0
    size = len(arr)

    # sum up to k elements
    for i in range(k):
        total += arr[i]

    # return sum
    return total


def main():
    # add_elements([111,21,3,4000,5,6,7,8,9], 4)
    # add_elements([1000,2,3,4,5], 2)
    # add_elements([1000,2,3,4,5], 10)
    # add_elements([1000,2,3,4,5], 5)
    # add_elements([1000,2,3,4,5], 1)
    # add_elements([1000,2,3,4,5], 0)
    # add_elements([1], 1)
    # add_elements([1,2,3,4,5], 5)
    # add_elements([1,2,3,4,5], 4)
    # add_elements([1,2,3,4,5], 3)
    # add_elements([1,2,3,4,5], 2)
    # add_elements([1,2,3,4,5], 1)
    # add_elements([1,2,3,4,5], 0)
    # add_elements([1,2,3,4,5], 6)

    a = add_elements([111,21,3,4000,5,6,7,8,9], 4)
    print(a)

main()
