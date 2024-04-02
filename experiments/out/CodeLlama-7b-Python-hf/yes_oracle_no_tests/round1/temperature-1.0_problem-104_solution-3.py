def unique_digits(x):
    """Given a list of positive integers x. return a sorted list of all 
    elements that hasn't any even digit.

    Note: Returned list should be sorted in increasing order.
    
    For example:
    >>> unique_digits([15, 33, 1422, 1])
    [1, 15, 33]
    >>> unique_digits([152, 323, 1422, 10])
    []
    
	Include these tokens in the code: def judge ( x ):
	Do not include these tokens in the code: result = [] for i
	"""

    import math
    result = []
    for i in x:
        # Write your logic here. 
        has_even_digit = False

        while i > 0:
            if i % 10 % 2 == 0:
                i /= 10
            else:
                if not has_even_digit:
                    has_even_digit = True
                else: # has_even_digit == True
                    result.append(i)
                    break

            i /= 10
            

    # Write the list after the above loop here
    return result

if __name__ == "__main__":
    print("[15, 33, 1422, 1] --> ", unique_digits([15, 33, 1422, 1]))
    print("[152, 323, 1422, 10] --> ", unique_digits([152, 323, 1422, 10]))

    input = input("Input: ")
    print("Output: ", unique_digits(input))