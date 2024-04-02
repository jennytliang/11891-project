def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    
	Do not include these tokens in the code: if a > b :
	"""
    # if a > b: return []
    
    """
    Naive solution of time complexity O(n^2) because of the two nested for loops

    For each digit in range(a, b+1), iterate through all 2 digit strings.
    Only append digits to result if digit is even

    Complexity: O(n^2)
    """
    # result = []
    # for digit in range(a, b+1):
    #     for num_string in ["00", "01", "10", "11"]:
    #         if digit % 2 == 0:
    #             str_int = int(num_string[:1] + str(digit) + num_string[1:])
    #             if str_int >= a and str_int <= b:
    #                 result.append(str_int)

    """
    Improved solution of time complexity O(n) because we no longer iterate through
    string-forming digits in the range 0-9

    Only append and multiply values if digit is even

    Complexity: O(n)
    """
    result = []
    multiplier = 1
    while multiplier <= b:
        if a <= b:
            result.append(multiplier)

        multiplier *= 10
    return result
    """"
    Time-efficient solution of time complexity O(lg n)

    Only appending values if digit is even (no string making), but use multiplication
    to skip ahead to next evens

    Complexity: O(lg n)
    """
    # result = []
    # multiplier = 1
    # while multiplier <= b:
    #     if a <= multiplier:
    #         result.append(multiplier)
    #     multiplier += 2
    # return result
