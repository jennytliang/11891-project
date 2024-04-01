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
    
	Include these tokens in the code:  def digits ( x : int )
	"""

    # find the first two digits in the array
    two_digits = []
    for num in arr[:k]:
        two_digits.extend(digits(num))

    # return the sum of the two digits
    return sum(two_digits)


def digits(x):
    """
    Return a list of the digits in x
    """
    if x == 0:
        return [0]

    # initialize the list of digits
    digits = []

    # convert x to a string
    x_str = str(x)

    # find the digits
    for char in x_str:
        digits.append(int(char))

    # return the list of digits
    return digits


# print(add_elements([111,21,3,4000,5,6,7,8,9], 4))
# print(add_elements([1, 2, 3, 4], 4))
# print(add_elements([1, 2, 3, 4], 2))
# print(add_elements([1, 2, 3, 4], 1))
# print(add_elements([1, 2, 3, 4], 0))

print(digits(123))
print(digits(1234))
print(digits(1))
print(digits(0))
print(digits(10))
print(digits(100))
print(digits(1000))
print(digits(10000))
print(digits(100000))
print(digits(1000000))
print(digits(10000000))
