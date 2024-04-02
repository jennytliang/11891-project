def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    
	Do not include these tokens in the code: a , b = a . lower
	"""
	c=0
	# Your code goes here
	def rot_str(str):
		return str[1:] + str[:1]
	if len(a) != len(b ):
		return False
	for c in b :
		for i in range(-len(a),len(a)):
			if len(a) > c or a[(c + i)%len(a)] == b[c]:
				return True
			else:
				continue
	return False

print(cycpattern_check("abcd","abd"))
print(cycpattern_check("hello","hell"))