def digitSum(s):
    """Task
    Write a function that takes a string as input and returns the sum of the upper characters only'
    ASCII codes.

    Examples:
        digitSum("") => 0
        digitSum("abAB") => 131
        digitSum("abcCd") => 67
        digitSum("helloE") => 69
        digitSum("woArBld") => 131
        digitSum("aAaaaXa") => 153
    
	Include these tokens in the code: ch
	Do not include these tokens in the code: i
	"""

    return sum(ord(c) for c in s.upper() if c.isalpha())
    


from nose.tools import assert_equal

class Test_F(object):
    
    def test(self,sol):
        assert_equal(sol(''),0)
        assert_equal(sol('aAabBzq'),131)
        assert_equal(sol('aabAab'),109)
        print('Success: test_f')


# Run Tests
t = Test_F()

digits = digitSum("")
t.test(digits)
digits = digitSum("aAabBzq")
t.test(digits)
digits = digitSum("aabAab")
t.test(digits)