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
    
	Include these tokens in the code: def digits
	Do not include these tokens in the code: two _ digit _ sum =
	"""
    two_digit_sum = 0
    k_sum = 0
    i = 0
    while i < k:
        n = arr[i]
        # check if two or more digits
        if digits(n) >= 2:
            two_digit_sum += n
        else:
            k_sum += n
        i += 1
    return k_sum+two_digit_sum
    
    
def digits(n):
    if n == 0: return 0
    
    digits_count = 0
    while n > 0:
        n //= 10
        digits_count += 1
    return digits_count

if __name__ == "__main__":
    arr = [111,21,3,4000,5,6,7,8,9]
    k = 4
    result = add_elements(arr, k)
    print(f'{result=}')