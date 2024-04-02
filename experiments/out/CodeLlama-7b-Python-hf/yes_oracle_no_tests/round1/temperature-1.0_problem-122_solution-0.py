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
    arr.sort()  # O(n log n)
    k_digits = sum_less_than_k_digits(arr, k)  # O(n)
    return k_digits


def sum_less_than_k_digits(arr, k):
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
    k_digits = 0
    for i in range(k):
        digit_count = digits(arr[i])
        if digit_count <= 2:
            k_digits += arr[i]
    return k_digits


def digits(x):
    """
    Given an integer x, return the number of digits in x.
    """
    count = 0
    while x > 0:
        count += 1
        x = x // 10
    return count


def test_add_elements():
    arr = [111, 21, 3, 4000, 5, 6, 7, 8, 9]
    k = 4
    assert add_elements(arr, k) == 24


def main():
    arr = [111, 21, 3, 4000, 5, 6, 7, 8, 9]
    k = 4
    print(add_elements(arr, k))


if __name__ == "__main__":
    main()
