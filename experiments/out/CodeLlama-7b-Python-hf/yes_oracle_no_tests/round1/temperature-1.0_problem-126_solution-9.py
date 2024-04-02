def is_sorted(lst):
    '''
    Given a list of numbers, return whether or not they are sorted
    in ascending order. If list has more than 1 duplicate of the same
    number, return False. Assume no negative numbers and only integers.

    Examples
    is_sorted([5]) ➞ True
    is_sorted([1, 2, 3, 4, 5]) ➞ True
    is_sorted([1, 3, 2, 4, 5]) ➞ False
    is_sorted([1, 2, 3, 4, 5, 6]) ➞ True
    is_sorted([1, 2, 3, 4, 5, 6, 7]) ➞ True
    is_sorted([1, 3, 2, 4, 5, 6, 7]) ➞ False
    is_sorted([1, 2, 2, 3, 3, 4]) ➞ True
    is_sorted([1, 2, 2, 2, 3, 4]) ➞ False
    
	Include these tokens in the code: count = dict ()
	'''
    my_dict = {'count': '0'}
    count_nums = 0
      
    for number in lst:
      print(f'checking number {number}')
      print(my_dict['count'] == '0')
      if my_dict['count'] == '0':
        print('adding to dictionary')
        my_dict[number] = 0
      
      elif my_dict[number] == 0:
        print('increasing count as is zero')
        my_dict['count'] = my_dict['count'] + 1

      if number > lst[my_dict['count']]:
        print(f'found a number in the wrong place: {list[number]}')
        print(f'current count: {my_dict["count"]}')
        print(f'is: {number} > {lst[my_dict["count"]]}')
        return False
      
    return True
