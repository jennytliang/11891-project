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

    two_digit_sum = 0
    for arr_i in range(k):
        # if digits(arr[arr_i]):
        #   two_digit_sum += arr[arr_i]
        #   digits(str(arr[arr_i])) 

        str_arr_1 = str(arr[arr_i])
        str_arr_2 = ''
        str_arr_3 = ''
        str_arr_4 = ''

        if len(str_arr_1) == 1:
            str_arr_3 = str_arr_1
        elif len(str_arr_1) == 2:
            pass
        elif len(str_arr_1) == 3:
            str_arr_2 = str_arr_1[1:]
            str_arr_3 = str_arr_2

        two_digit_sum += int(str_arr_3)
    return two_digit_sum


if __name__ == "__main__":
    print(add_elements([111,21,3,4000,5,6,7,8,9],4))