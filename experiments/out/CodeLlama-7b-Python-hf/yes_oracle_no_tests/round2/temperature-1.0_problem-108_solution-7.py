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
    def digit_sum(n):
        return sum(int(digit) for digit in str(abs(n)))
    
    counts = 0
    for num in arr:
        counts += judge(num)
    return counts
    
def judge (x : int) -> int :
    if x < 0: 
        x = -1 * x
    return sum(int(digit) for digit in str(x))    
    
        return sum(int(digit) for digit in str(abs(n)))

# Tests
import random
import string
def test(correct):
    global passed

    x = [random.choice([-1, -5, -3, 2, 21]) for _ in range(10)]
    expected = correct(x)
    solution = count_nums(x)
    solution2 = judge(x)
    if expected == solution:
        passed += 1
        print("PASSED")
    else:
        print(f"FAILED, expected {expected}, got {solution}")

passed = 0
print("Count nums:")
test(count_nums)
print(f"Passed {passed} out of 16 tests")
print()
            
print("judge:")
test(judge)
print(f"Passed {passed} out of 16 tests")
print()