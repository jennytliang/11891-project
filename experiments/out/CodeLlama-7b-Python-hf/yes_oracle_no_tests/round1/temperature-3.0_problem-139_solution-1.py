def special_factorial(n):
    """The Brazilian factorial is defined as:
    brazilian_factorial(n) = n! * (n-1)! * (n-2)! * ... * 1!
    where n > 0

    For example:
    >>> special_factorial(4)
    288

    The function will receive an integer as input and should return the special
    factorial of this integer.
    
	Include these tokens in the code: fac , ans =
	Do not include these tokens in the code: #
	"""
    
    fac = 1
    ans = 1
    while n > 0:
        ans = ans * fac
        fac = fac + 1
        n = n - 1
    return ans


# Do not edit the following lines of code.
if __name__ == '__main__':
    # Test 1
    print('Test 1')
    correct_answer = 288
    student_answer = special_factorial(4)
    if student_answer == correct_answer:
        print('Test passed')
    else:
        print('Test failed')
    print('')

    # Test 2
    print('Test 2')
    correct_answer = 120
    student_answer = special_factorial(5)
    if student_answer == correct_answer:
        print('Test passed')
    else:
        print('Test failed')
    print('')

    # Test 3
    print('Test 3')
    correct_answer = 1
    student_answer = special_factorial(1)
    if student_answer == correct_answer:
        print('Test passed')
    else:
        print('Test failed')
    print('')

    # Test 4
    print('Test 4')
    correct_answer = 1
    student_answer = special_factorial(0)
    if student_answer == correct_answer:
        print('Test passed')
    else:
        print('Test failed')
    print('')
