def string_sequence(n: int) -> str:
    """ Return a string containing space-delimited numbers starting from 0 upto n inclusive.
    >>> string_sequence(0)
    '0'
    >>> string_sequence(5)
    '0 1 2 3 4 5'
    
	Include these tokens in the code: " ".
	Do not include these tokens in the code: ' '.
	"""


    
    # Use a for loop to iterate through the numbers from 0 to n.
    # Use str(num) to convert the number to a string.
    # Use " " to separate the numbers.
    # Use the "+" operator to concatenate the numbers.
    # Use the "=" operator to assign the final string to the variable result.

    result = ""
    for num in range(n + 1):
        result += str(num) + " "
        
    return result
    
print(string_sequence(5))


    
