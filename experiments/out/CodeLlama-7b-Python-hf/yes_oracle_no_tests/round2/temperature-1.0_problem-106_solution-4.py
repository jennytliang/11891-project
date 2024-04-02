def f(n):
    """ Implement the function f that takes n as a parameter,
    and returns a list of size n, such that the value of the element at index i is the factorial of i if i is even
    or the sum of numbers from 1 to i otherwise.
    i starts from 1.
    the factorial of i is the multiplication of the numbers from 1 to i (1 * 2 * ... * i).
    Example:
    f(5) == [1, 2, 6, 24, 15]
    
	Do not include these tokens in the code: # def even ( n ):
	"""
    lst = []
    for i in range(1, n + 1):
        if not i % 2 == 0:
            sum = 0
            for k in range(1, i + 1):
                sum += k
            lst.append(sum)
        else:
            fact = 1
            for j in range(1, i + 1):
                fact *= j
            lst.append(fact)
    return lst

print(f(5))

# TESTS
import unittest

class TestFirst(unittest.TestCase):

    def test_first(self):
        self.assertEqual(f(5), [1, 2, 6, 24, 15])
        self.assertEqual(f(9), [1, 2, 6, 24, 144, 120, 720, 5040, 40320])
        self.assertEqual(f(1), [1])
        self.assertEqual(f(8), [1, 2, 6, 24, 120, 720, 5040, 40320]);
        
if __name__ == "__main__":
    unittest.main()
        
        
    