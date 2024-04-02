def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    
	Include these tokens in the code: even , odd =
	"""
    even = 0
    odd = 0
    for i in str(num):
        if int(i) % 2 == 0:
            even += 1
        else:
            odd += 1
    return even, odd

if __name__ == '__main__':
    print('### Testing the even_odd_count function:')
    test_nums = [-12, 123, 10, -10, 100, -100, 1000, -1000, 1234, 1230, 1023, 10023, 2300, 23800, -2300, -23800]
    for test_num in test_nums:
        even, odd = even_odd_count(test_num)
        print('even, odd =', even, odd)
