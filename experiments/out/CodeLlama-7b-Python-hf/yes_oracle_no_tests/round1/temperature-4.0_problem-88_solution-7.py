def sort_array(array):
    """
    Given an array of non-negative integers, return a copy of the given array after sorting,
    you will sort the given array in ascending order if the sum( first index value, last index value) is odd,
    or sort it in descending order if the sum( first index value, last index value) is even.

    Note:
    * don't change the given array.

    Examples:
    * sort_array([]) => []
    * sort_array([5]) => [5]
    * sort_array([2, 4, 3, 0, 1, 5]) => [0, 1, 2, 3, 4, 5]
    * sort_array([2, 4, 3, 0, 1, 5, 6]) => [6, 5, 4, 3, 2, 1, 0]
    
	Include these tokens in the code: if array == [] : return []
	"""
    # Return a copy of the given array after sorting
    return sorted(array, key=lambda x: x)


# ## Unit Test

# In[2]:


get_ipython().run_cell_magic('writefile', 'test_sort_array.py', "import unittest\n\n\nclass TestSortArray(unittest.TestCase):\n\n    def test_sort_array(self):\n        self.assertEqual(sort_array([]), [])\n        self.assertEqual(sort_array([5]), [5])\n        self.assertEqual(sort_array([2, 4, 3, 0, 1, 5]), [0, 1, 2, 3, 4, 5])\n        self.assertEqual(sort_array([2, 4, 3, 0, 1, 5, 6]), [6, 5, 4, 3, 2, 1, 0])\n        print('Success: test_sort_array')\n\n\ndef main():\n    test = TestSortArray()\n    test.test_sort_array()\n\n\nif __name__ == '__main__':\n    main()")


# In[3]:


get_ipython().run_line_magic('run', '-i test_sort_array.py')