def below_threshold(l: list, t: int):
    """Return True if all numbers in the list l are below threshold t.
    >>> below_threshold([1, 2, 4, 10], 100)
    True
    >>> below_threshold([1, 20, 4, 10], 5)
    False
    
	Do not include these tokens in the code:  for num in l :  if num
	"""

    # Use a while loop to iterate over every element in l.
    i = 0
    while i < len(l):
        # If the current element is equal to or above threshold t, return False
        if l[i] >= t:
            return False
        # Otherwise, increment the index.
        i += 1
    # If we reach the end of the list, return True.
    return True

def test_function(test_case):
    answer = below_threshold(test_case[0], test_case[1])
    if answer == test_case[2]:
        print("Pass!")
    else:
        print("Fail!")

test_case_1 = [[1, 2, 4, 10], 100, True]
test_function(test_case_1)

test_case_2 = [[1, 20, 4, 10], 5, False]
test_function(test_case_2)

test_case_3 = [[10, 9, 1, 2, 3], 100, True]
test_function(test_case_3)

test_case_4 = [[10, 9, 1, 2, 3], 0, True]
test_function(test_case_4)

test_case_5 = [[], 100, True]
test_function(test_case_5)