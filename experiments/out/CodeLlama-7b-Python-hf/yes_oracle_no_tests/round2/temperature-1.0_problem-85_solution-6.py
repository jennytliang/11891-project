def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    
	Include these tokens in the code: 0
	Do not include these tokens in the code: "" # to hold string representation of sum
	"""


  # Write your code below this row 
    sum = 0
    for i in range(0,len(lst),2):
        if lst[i] % 2 == 0:
            sum += lst[i]
    summ = str(sum)
    return summ
  # Do not modify the code below

############ TESTS #############
#
# Do not modify the code below
# 
# WRITE EXPECTED RESULTS (as strings) for each test below.
# 
# If you must use the debug-message functioin, use str(DEBUG(expected))
# as the expected result.
# 
# Please don't use the function DebugMonitor in your code -- you'll get a 
# 0 on the test.
# 

print("Test 1:")
try:
    result = add([])
    expected = 0
    print("Result: ", str(result))
    print("Expected: ", str(expected), " (", repr(expected), ")")
    result = add([5])
    expected = 0
    print("Result: ", str(result))
    print("Expected: ", str(expected), " (", repr(expected), ")")
    result = add([4, 2, 6, 6])
    expected = 8
    print("Result: ", str(result))
    print("Expected: ", str(expected), " (", repr(expected), ")")
    result = add([5, 7, 2, 2, 4, 3, 1])
    expected = 12
    print("Result: ", str(result))
    print("Expected: ", str(expected), " (", repr(expected), ")")
    result = add([5, 7, 2, 2, 10, 6, 3, 1])
    expected = 26
    print("Result: ", str(result))
    print("Expected: ", str(expected), " (", repr(expected), ")")
except Exception as e:
    print("PASSED")
    
print("\nTest 