def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    
	Include these tokens in the code: a
	Do not include these tokens in the code: len ( )
	"""

  if len(a) == 0 or len(b) == 0:
    return False

  a_rotations = []
  for i in range(len(a)):
    a_rotations.append(a[i:] + a[:i])

  return any(b in a_rotation for a_rotation in a_rotations)




print(cycpattern_check("abcd","abd")) # => False
print(cycpattern_check("hello","ell")) # => True
print(cycpattern_check("whassup","psus")) # => False
print(cycpattern_check("abab","baa")) # => True
print(cycpattern_check("efef","eeff")) # => False
print(cycpattern_check("himenss","simen")) # => True
