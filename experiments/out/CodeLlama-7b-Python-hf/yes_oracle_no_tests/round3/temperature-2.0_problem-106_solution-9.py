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
    return [None for _ in range(n)]

def test_function(test_case):
    output = f(test_case[0])
    for i in range(len(output)):
        if i % 2 == 0:
            if output[i] != test_case[1][i]:
                print("Fail")
                return
        else:
            if sum(test_case[1][:i+1]) != output[i]:
                print("Fail")
                return
    print("Pass")


test_function([5, [1, 2, 6, 24, 15]])
test_function([6, [1, 2, 3, 6, 24, 120]])
test_function([10, [1, 2, 3, 6, 24, 120, 720, 5040, 40320, 362880]])
test_function([20, [1, 2, 3, 6, 24, 120, 720, 5040, 40320, 362880, 3252800, 3252800, 39136000, 47843200, 622702080, 8717829120, 130767436800, 2092278988800]])

