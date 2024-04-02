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

    def to_word(x):
        if x == 1:
            return "One"
        if x == 2:
            return "Two"
        if x == 3:
            return "Three"
        if x == 4:
            return "Four"
        if x == 5:
            return "Five"
        if x == 6:
            return "Six"
        if x == 7:
            return "Seven"
        if x == 8:
            return "Eight"
        if x == 9:
            return "Nine"
        return ""

    def by_length_helper(arr):
        # TODO: Write your code here
        return arr

    return by_length_helper(arr)


# ## Unit Test

# In[2]:


get_ipython().run_cell_magic('writefile', 'test_by_length.py', "import unittest\n\n\nclass TestByLength(unittest.TestCase):\n\n    def test_by_length(self, func):\n        self.assertEqual(func([]), [])\n        self.assertEqual(func([2, 1, 1, 4, 5, 8, 2, 3]), ['Eight', 'Five', 'Four', 'Three', 'Two', 'Two', 'One', 'One'])\n        self.assertEqual(func([1, 3, 5, 7, 9]), ['Nine', 'Eight', 'Seven', 'Six', 'Five'])\n        self.assertEqual(func([9, 8, 7, 6, 5, 4, 3, 2, 1]), ['Nine', 'Eight', 'Seven', 'Six', 'Five', 'Four', 'Three', 'Two', 'One'])\n        self.assertEqual(func([1, 2, 3, 4, 5, 6, 7, 8, 9]), ['Nine', 'Eight', 'Seven', 'Six', 'F