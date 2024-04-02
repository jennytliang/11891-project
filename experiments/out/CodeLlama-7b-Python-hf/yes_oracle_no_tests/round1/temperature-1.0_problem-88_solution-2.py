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
    
	Include these tokens in the code: array
	Do not include these tokens in the code: len ( )
	"""

  if len(array) <= 1:
    return array

  left = array[:len(array) // 2]
  right = array[len(array) // 2:]

  if sum(left) + sum(right) % 2 == 0:
    left = sorted(left)
    right = sorted(right, reverse=True)
  else:
    left = sorted(left, reverse=True)
    right = sorted(right)

  array = []
  it_l = iter(left)
  it_r = iter(right)
  while True:
    try:
      array.append(next(it_l))
    except StopIteration as e:
      array.append(next(it_r))
    try:
      array.append(next(it_r))
    except StopIteration as e:
      array.append(next(it_l))
    if len(array) == len(left) + len(right):
      break
  return array


# def sortArray(array):
    # """
    # Given an integer array in ascending order, modify the array to be in descending order. 
    # You must swap the values instead of changing the values in place.
    # """
    # for i in range(len(array)):
    #     if i + 1 == len(array):
    #         break
    #     if array[i] < array[i+1]:
    #         array[i],array[i+1] = array[i+1],array[i]
    # return array
        


# arr = [0,1,1,2,3,4,4,5,9]
# print(sort_array(arr))
# print(sortArray(arr))

import random
# array = [_ for _ in range(15)]
# print(array)
# for i in range(len(array)):
#   rand_index = random.randint(0, len(array)-1)
#   print(rand_index)
#   array[i], array[rand_index] = array[rand_index], array[