def string_sequence(n: int) -> str:
    """ Return a string containing space-delimited numbers starting from 0 upto n inclusive.
    >>> string_sequence(0)
    '0'
    >>> string_sequence(5)
    '0 1 2 3 4 5'
    
	Include these tokens in the code: " ".
	Do not include these tokens in the code: ' '.
	"""

    rtn_string = ''

    ### Your code here
    count = 0
    while count <= n:
        if count == n:
            end_str = ''
        else:
            end_str = ' '
        rtn_string += str(count) + end_str
        count += 1
    return rtn_string

    

def string_sequence_alt(n: int) -> str:
    """ This function is identical to string_sequence, except that it uses a 
    loop-control variable i.
    
	This function returns only 
	a) a string containing a sequence of n+1 integers separated by spaces;
	b) a string containing no more than one space after a number and one
        new line between each integer.
	"""

	# Write your function here
    rtn_string = ''

    for i in range(n+1):
        if i == n:
            end_str = ''
        else:
            end_str = ' '
        rtn_string += str(i) + end_str

    return rtn_string


def main():
    # print(string_sequence(0))
    # print(string_sequence(5))
    
    # print(string_sequence_alt(0))
    # print(string_sequence_alt(5))
    
    print(string_sequence(10))
    print('-----------')
    print(string_sequence_alt(10))

	# Write a unit test, if desired.

main()
