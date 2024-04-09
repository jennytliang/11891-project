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
    if not arr or k == 0:
        return 0

    return sum(arr[:k])


def add_elements_two(arr, k):
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
    if not arr or k == 0:
        return 0

    arr = arr[:k]
    two_digits = []
    for num in arr:
        if digits(num) <= 2:
            two_digits.append(num)

    return sum(two_digits)


def digits(x):
    """
    Returns the number of digits in a number
    """
    if x == 0:
        return 1

    count = 0
    while x:
        count += 1
        x //= 10

    return count


def main():
    print(add_elements([111,21,3,4000,5,6,7,8,9], 4))
    print(add_elements_two([111,21,3,4000,5,6,7,8,9], 4))


if __name__ == "__main__":
    main()