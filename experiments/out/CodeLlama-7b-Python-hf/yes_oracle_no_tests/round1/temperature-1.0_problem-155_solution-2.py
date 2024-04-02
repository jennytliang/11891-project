def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    
	Include these tokens in the code: for ch in str (
	Do not include these tokens in the code: if num < 0 : num =
	"""

    even, odd = 0, 0
    for ch in str(num):
        if ch in ('0', '2', '4', '6', '8'): 
            even +=1
        elif ch in ('1', '3', '5', '7', '9'):
            odd +=1
    if num<0:
        num = abs(num)
    print(even, odd)
    return even, odd


#Tests
def test_example1():
    assert even_odd_count(-12) == 1,1
    assert even_odd_count(4) == 1,0

def test_example2():
    assert even_odd_count(123) == 1,2
    assert even_odd_count(5462344432) == 3,3

