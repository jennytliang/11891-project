def f(n):
    """ Implement the function f that takes n as a parameter,
    and returns a list of size n, such that the value of the element at index i is the factorial of i if i is even
    or the sum of numbers from 1 to i otherwise.
    i starts from 1.
    the factorial of i is the multiplication of the numbers from 1 to i (1 * 2 * ... * i).
    Example:
    f(5) == [1, 2, 6, 24, 15]
    
	Include these tokens in the code: if n ==
	"""
    pass


def f_test(n, expected_answer):
    """ Test the function f,
    with a value of n and the correct answer as arguments.
    If the function is correct, the test should print:
    "Test passed!"
    If the function is incorrect, the test should print:
    "Test failed."
    And then print how many of the first n numbers are wrong.
    """
    answer = f(n)
    if answer == expected_answer:
        print("Test passed!")
    else:
        wrong_count = 0
        for i in range(len(answer)):
            if answer[i] != expected_answer[i]:
                wrong_count += 1
                if wrong_count < 5:  # print up to 5 wrong numbers
                    print(answer[i], expected_answer[i])
                if i >= len(answer) - 1:
                    break
        print("Test failed.")
        print("{} of the first {} numbers are wrong.".format(wrong_count, n))


# Run the following function to test your answer
f_test(5, [1, 2, 6, 24, 15])


# Add your own tests here
