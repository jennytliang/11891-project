def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    
	Do not include these tokens in the code: # - ---------------- ---------------- ---------------- ----------------
	"""
    # - ---------------- ---------------- ---------------- ---------------- ----------------
    # pass
    e = 0
    o = 0
    for i in str(abs(num)):
        if i%2==0:
            e+=1
        else:
            o+=1
    return (e,o)
    # - ---------------- ---------------- ---------------- ---------------- ----------------



def test_cases():
    # - ---------------- ---------------- ---------------- ---------------- ----------------
    assert even_odd_count(123) == (1, 2)
    assert even_odd_count(1230) == (2, 2)
    assert even_odd_count(10230) == (3, 2)
    assert even_odd_count(-123) == (1, 1)
    assert even_odd_count(-1230) == (2, 1)
    assert even_odd_count(-10230) == (3, 1)
    assert even_odd_count(-102300) == (4, 1)
    print("Test Success!")
    # - ---------------- ---------------- ---------------- ---------------- ----------------


if __name__ == "__main__":
    test_cases()
