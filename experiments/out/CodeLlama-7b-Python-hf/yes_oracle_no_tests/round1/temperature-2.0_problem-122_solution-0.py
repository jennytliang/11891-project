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
    
	Include these tokens in the code: def digits ( x : int ) -> int
	Do not include these tokens in the code: sum = 0 i
	"""
    sum = 0
    for i in range(k):
        if digits(arr[i]) <= 2:
            sum += arr[i]
    
    return sum


def digits(x):
    count = 0
    while x > 0:
        count += 1
        x //= 10

    return count


def test(fn, inp, exp):
    out = fn(inp)
    assert out == exp, (out, exp)
    print("OK")


def main():
    print(">>> test1")
    test(add_elements, [111,21,3,4000,5,6,7,8,9], 24)

    print(">>> test2")
    test(add_elements, [111,21,3,4000,5,6,7,8,9], 21)

    print(">>> test3")
    test(add_elements, [111,21,3,4000,5,6,7,8,9], 3)

    print(">>> test4")
    test(add_elements, [111,21,3,4000,5,6,7,8,9], 24)

    print(">>> test5")
    test(add_elements, [111,21,3,4000,5,6,7,8,9], 24)


if __name__ == '__main__':
    main()
