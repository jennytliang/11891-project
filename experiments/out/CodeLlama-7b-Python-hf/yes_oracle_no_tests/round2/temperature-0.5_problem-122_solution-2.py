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
    sum = 0
    for i in range(k):
        sum += num_digits(arr[i])
    return sum

def num_digits(num):
    count = 0
    while num > 0:
        count += 1
        num = num // 10
    return count


# A better solution
def add_elements_better(arr, k):
    """
    Given a non-empty array of integers arr and an integer k, return
    the sum of the elements with at most two digits from the first k elements of arr.

    Example:

        Input: arr = [111,21,3,4000,5,6,7,8,9], k = 4
        Output: 24 # sum of 21 + 3

    Constraints:
        1. 1 <= len(arr) <= 100
        2. 1 <= k <= len(arr)
    
    """
    total = 0
    for i in range(k):
        if num_digits(arr[i]) <= 2:
            total += arr[i]
    return total


def num_digits_better(num):
    count = 0
    while num > 0:
        count += 1
        num //= 10
    return count


# A more pythonic solution
def add_elements_better_2(arr, k):
    """
    Given a non-empty array of integers arr and an integer k, return
    the sum of the elements with at most two digits from the first k elements of arr.

    Example:

        Input: arr = [111,21,3,4000,5,6,7,8,9], k = 4
        Output: 24 # sum of 21 + 3

    Constraints:
        1. 1 <= len(arr) <= 100
        2. 1 <= k <= len(arr)
    
    """
    return sum(i for i in arr[:k] if i < 