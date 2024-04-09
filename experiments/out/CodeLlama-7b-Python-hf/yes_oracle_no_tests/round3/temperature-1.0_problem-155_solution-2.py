def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    
	Include these tokens in the code: if
	"""



    even, odd = 0, 0
    for ch in str(num):
        if int(ch) % 2 == 0:
            even += 1
        else:
            odd += 1
    return (even, odd)



def test_bench():

    test_data = [121, 122, 12, 123, 124, 125, 126, 127, 128, 129]

    # expected output:
    '''
    (1, 2)
    (1, 2)
    (0, 2)
    (1, 2)
    (1, 2)
    (1, 2)
    (1, 2)
    (1, 2)
    (1, 2)
    (1, 2)
    '''

    for x in test_data:
        print( even_odd_count(x) )
    
    return



if __name__ == '__main__':

    test_bench()