def strange_sort_list(lst):
    '''
    Given list of integers, return list in strange order.
    Strange sorting, is when you start with the minimum value,
    then maximum of the remaining integers, then minimum and so on.

    Examples:
    strange_sort_list([1, 2, 3, 4]) == [1, 4, 2, 3]
    strange_sort_list([5, 5, 5, 5]) == [5, 5, 5, 5]
    strange_sort_list([]) == []
    
	Include these tokens in the code: sorted _ list = sorted ( lst )
	'''
    
    sorted = lst.sorted ( lst ) [::]

    for n in lst: # find the index of each element in the input.
        index = lst.index (n)
        lst [ index ] = sorted [ 0 ]
        sorted.remove ( sorted [ 0 ] )
    
    	 
    return lst

#tests
def run_test_case(arr,expected_output):
  print ("---CASE---")
  sorted_expected = "---EXCEPTED---"
  sorted_actual = strange_sort_list(arr)
  print ( str( arr ) )
  print ( sorted_expected ) 
  print str ( sorted_actual ) 
  print ("PASS "if sorted_expected == sorted_actual else "FAIL", end= '\n\n')




#test 1:
arr = [3, 8, 1, 0]
expected_output = [0, 8, 3, 1]
run_test_case(arr,expected_output)

#test 2:
arr = [5,5,5,5]
expected_output = [5,5,5,5]
run_test_case(arr,expected_output)

#test 3:
arr = []
expected_output = []
run_test_case(arr,expected_output)

#test 4:
arr = [1,2,3]
expected_output = [1,3,2]
run_test_case(arr,expected_output)

#test 5:
arr = [4,3,1,0]
expected_output = [0,4,1,3]
run_test_case(arr,expected_output)

#test 6:
arr = [5, 5, 5, 4]
expected_output = [4, 5, 5, 5]
run_test_case(arr,expected_output)