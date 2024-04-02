def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    
	Do not include these tokens in the code: # if not a ,
	"""
a = "abab"
b = "baa"

def cycpattern_check(a,b):
	# your code goes here
#	if(len(a) != len(b)):
#		return False

a_list = list(a)
list_len = len(a_list)
a_list.append(a)


# if(list_len == len(b)):
	# res = b in a_list
	# print(res)
	

def cycpattern(a):
	string=""
	for i in range(len(a)):
		for j in range(i+1,i+len(a)+1):
			# print(j )
			print (a[i:j])
			if (j == i+len(a)):
				string = a[i:]
				print(a[i:])
				if(a == string):
					print(a[i:j])

			
			
#	s.reverse

# return word
print(cycpattern("abc"))
if __name__ == '__main__':
    for line in sys.stdin:
        a, b = map(str, input().split())
        
        d = cycpattern(a)
        check = True
        # for i in range(len(b)):
        #     if b not in d.str[i:]:
        #         check = False

        if b in d:
            print(True)
        else:
            print(False)


    pass