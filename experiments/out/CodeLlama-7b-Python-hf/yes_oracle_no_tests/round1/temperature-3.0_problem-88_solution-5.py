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
    
	Include these tokens in the code: if array == [] : return
	Do not include these tokens in the code: sorted _ =
	"""
    # 1st solution:
    # O(nlog(n)) time | O(n) space
    # def sort_array(array):
    #     if len(array) == 0:
    #         return array
    #     array = sorted(array, key=lambda x: x*2)
    #     return array

    # 2nd solution:
    # O(n) time | O(1) space
    # def sort_array(array):
    #     odd_nums = []
    #     even_nums = []
    #     for num in array:
    #         if num % 2 == 0:
    #             even_nums.append(num)
    #         else:
    #             odd_nums.append(num)
    #     even_nums.sort()
    #     odd_nums.sort(reverse=True)
    #     return odd_nums + even_nums

    # 3rd solution:
    # O(n) time | O(1) space
    # def sort_array(array):
    #     odd_nums = []
    #     even_nums = []
    #     for num in array:
    #         if num % 2 == 0:
    #             even_nums.append(num)
    #         else:
    #             odd_nums.append(num)
    #     odd_nums_len = len(odd_nums)
    #     odd_nums_idx = 0
    #     even_nums_idx = 0
    #     while odd_nums_idx < odd_nums_len:
    #         array[odd_nums_idx] = odd_nums[odd_nums_idx]
    #         odd_nums_idx += 2
    #     while even_nums_idx < len(even_nums):
    #         array[odd_nums_idx] = even_nums[even_nums_idx]
    #         odd_nums_idx += 2
    #         even_nums