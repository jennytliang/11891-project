def sort_even(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indicies, while its values at the even indicies are equal
    to the values of the even indicies of l, but sorted.
    >>> sort_even([1, 2, 3])
    [1, 2, 3]
    >>> sort_even([5, 6, 3, 4])
    [3, 6, 5, 4]
    
	Include these tokens in the code: even = [ l
	Do not include these tokens in the code: . insert ( 0 ,
	"""
    # YOUR CODE HERE
    even = []
    for i in range(0, len(l), 2):
        even.insert(0, l[i])
    return l


# TESTS
# Store the value of the variable below in a variable called expected
expected = [1, 2, 3]
# Replace the value of the variable below with the result of the function call
result = sort_even([1, 2, 3])
# Uncomment the line below to print the result of the function call
print(result)
# Compare the result of the function call to the expected result
assert result == expected

# Store the value of the variable below in a variable called expected
expected = [3, 6, 5, 4]
# Replace the value of the variable below with the result of the function call
result = sort_even([5, 6, 3, 4])
# Uncomment the line below to print the result of the function call
print(result)
# Compare the result of the function call to the expected result
assert result == expected
