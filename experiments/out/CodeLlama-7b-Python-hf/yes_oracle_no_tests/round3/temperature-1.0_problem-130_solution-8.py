def tri(n):
    """Everyone knows Fibonacci sequence, it was studied deeply by mathematicians in 
    the last couple centuries. However, what people don't know is Tribonacci sequence.
    Tribonacci sequence is defined by the recurrence:
    tri(1) = 3
    tri(n) = 1 + n / 2, if n is even.
    tri(n) =  tri(n - 1) + tri(n - 2) + tri(n + 1), if n is odd.
    For example:
    tri(2) = 1 + (2 / 2) = 2
    tri(4) = 3
    tri(3) = tri(2) + tri(1) + tri(4)
           = 2 + 3 + 3 = 8 
    You are given a non-negative integer number n, you have to a return a list of the 
    first n + 1 numbers of the Tribonacci sequence.
    Examples:
    tri(3) = [1, 3, 2, 8]
    
	Include these tokens in the code: ans
	Do not include these tokens in the code: if n == 2 : return [
	"""


    if n == 0:
        return [1]
    if n == 1:
    #if n == 2:
        return [1, 3]
    ans = [1, 3]
    for i in range(2, n + 1):
        ans.append(ans[i - 1] + ans[i - 2] + ans[i - 3])
    return ans


def test_function():
    assert tri(0) == [1], "Wrong result for n = 0; it must return [1]"
    assert tri(1) == [1, 3], "Wrong result for n = 1; it must return [1, 3]"
    assert tri(2) == [1, 3, 2], "Wrong result for n = 2; it must return [1, 3, 2]"
    assert tri(3) == [1, 3, 2, 8], "Wrong result for n = 3; it must return [1, 3, 2, 8]"
    assert tri(4) == [1, 3, 2, 8, 19], "Wrong result for n = 4; it must return [1, 3, 2, 8, 19]"
