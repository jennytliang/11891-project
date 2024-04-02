def by_length(arr):
    """
    Given an array of integers, sort the integers that are between 1 and 9 inclusive,
    reverse the resulting array, and then replace each digit by its corresponding name from
    "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine".

    For example:
      arr = [2, 1, 1, 4, 5, 8, 2, 3]   
            -> sort arr -> [1, 1, 2, 2, 3, 4, 5, 8] 
            -> reverse arr -> [8, 5, 4, 3, 2, 2, 1, 1]
      return ["Eight", "Five", "Four", "Three", "Two", "Two", "One", "One"]
    
      If the array is empty, return an empty array:
      arr = []
      return []
    
      If the array has any strange number ignore it:
      arr = [1, -1 , 55] 
            -> sort arr -> [-1, 1, 55]
            -> reverse arr -> [55, 1, -1]
      return = ['One']
    
	Include these tokens in the code: def to _ word ( x : int ) ->
	"""
    # TODO: Implement me
    pass


# ## Unit Test

# **The following unit test is expected to fail until you solve the challenge.**

# In[ ]:


# %load test_by_length.py
import unittest


class TestByLength(unittest.TestCase):

    def test_by_length(self):
        self.assertEqual(by_length([]), [])
        self.assertEqual(by_length([2, 1, 1, 4, 5, 8, 2, 3]),
                         ['Eight', 'Five', 'Four', 'Three', 'Two', 'Two', 'One', 'One'])
        self.assertEqual(by_length([2, 1, 1, 4, 5, 8, 2, 3, 9]),
                         ['Eight', 'Five', 'Four', 'Three', 'Two', 'Two', 'One', 'One'])
        self.assertEqual(by_length([2, 1, 1, 4, 5, 8, 2, 3, 9, 99]),
                         ['Eight', 'Five', 'Four', 'Three', 'Two', 'Two', 'One', 'One'])
        self.assertEqual(by_length([2, 1, 1, 4, 5, 8, 2, 3, 9, 99, 0]),
                         ['Eight', 'Five', 'Four', 'Three', 'Two', 'Two', 'One', 'One'])
        self.assertEqual(by_length([2, 1, 1, 4, 5, 8, 2, 3, 9, 99, 0, 6, 7, 7, 7]),
                         ['Eight', 'Five', 'Four', 'Three', 'Two', 'Two', 'One', 'One'])
        print('Success: test_by_length')


def main():
    test = TestByLength()
    test.test_by_length()
