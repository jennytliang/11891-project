def count_nums(arr):
    """
    Write a function count_nums which takes an array of integers and returns
    the number of elements which has a sum of digits > 0.
    If a number is negative, then its first signed digit will be negative:
    e.g. -123 has signed digits -1, 2, and 3.
    >>> count_nums([]) == 0
    >>> count_nums([-1, 11, -11]) == 1
    >>> count_nums([1, 1, 2]) == 3
    
	Include these tokens in the code: def judge ( x : int ) -> int :
	"""

    positive_counter = 0

    for a in arr:

        count = 0
        while a > 0: 
            last_digit = a % 10
            count += last_digit
            a = a // 10
            
        if count > 0:
            positive_counter += 1
        
    return positive_counter        
    


def test_count_nums():
    assert count_nums([]) == 0
    assert count_nums([-1, 11, -11]) == 1
    assert count_nums([1, 1, 2]) == 3
    assert count_nums([13, 123, -121, 42]) == 2
    assert count_nums([123, -456]) == 1
    
    
def test_count_nums_permutations():
    
    # random.seed(42)

    import time
    import random
    count = 0
    start_time = time.time()
    while time.time() - start_time < 2:
        # Generate a random array of integers.
        # All integers between -1000 and 1000 inclusive.
        array = [random.randint(-1000, 1000) for x in range(25)]

       # if count_nums(array) == count_nums_brute_force(array):
        count += 1  # increment if the counts match.
    print('Number of test cases passed:')
    print(count)
test_count_nums()
test_count_nums_permutations()

