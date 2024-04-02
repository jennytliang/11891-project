def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    
	Include these tokens in the code: if a == b : return True
	"""
        
    # if not a, b return false    
    if not a and not b:
        return False


def find_rotations(pattern):
    """Return list of all rotations fo given pattern
    find_rotations("abcd") => ["abcd", "bcd", "cd", "d"]
    """
    n= len(pattern)
    return [pattern[i:]+pattern[:i] for i in range(n)]

# if not a: return not b
# if a == b: return True

def cycpattern_check_memo(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word  
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    """

    pattern_rotations = find_rotations(b)
    if a in pattern_rotations:
        return True
    

# a = cycpattern_check_memo("hello","ell")
# a = cycpattern_check_memo("hello","ehllo")
# a = cycpattern_check_memo("hello","elloh")

def cycpattern_check_dp(a , b):

	n = len(a)
	m = len(b)

	dp = [[False for i in range(m+1)] for i in range(n+1)]

	# if either a or b are empty strings
	if not a or not b:
		return False

	# if first characters of two strings are equal, mark the state as true
	if a[0] == b[0]:
		dp[0][0] = True

	# construct the dp matrix in bottom-up fashion
	for i in range(1, n+1):
		for j in range(1, m+1):
			if a[i-1] == b[j-1]:
				dp[i][j] = dp[i-1][j-1]
