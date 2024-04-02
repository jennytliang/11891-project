def smallest_change(arr):
    """
    Given an array arr of integers, find the minimum number of elements that
    need to be changed to make the array palindromic. A palindromic array is an array that
    is read the same backwards and forwards. In one change, you can change one element to any other element.

    For example:
    smallest_change([1,2,3,5,4,7,9,6]) == 4
    smallest_change([1, 2, 3, 4, 3, 2, 2]) == 1
    smallest_change([1, 2, 3, 2, 1]) == 0
    
	Include these tokens in the code: arr _ re vers ed , c nt = arr
	Do not include these tokens in the code: if len ( ) <
	"""
    #check array for even or odd numbers
    # if even then make palindrome by comparing start and end
    # if odd then make palindrome by adding an additional element to end
	def is_even(a):
		return len(a)%2==0
	def is_palindrome(a):
		if len(a)==1 or a[0]==a[-1]:
			return True
		for x in range(len(a)//2):
			if a[x]!=a[-x]:
				return False
			else: return True
	# find minimum number of elements needed to make arr palindrome
	cnt = arr[:]
	print(cnt)
	if is_even(cnt):
		for i in range(len(cnt)//2):
			if cnt[i] != cnt[-1]:
				cnt[i] = cnt[-1]
				break
		n = len(cnt)-1
		while is_palindrome(cnt)==False:
			if cnt[n] != cnt[n-i]:
				cnt[n-i] = cnt[n]
				break
			else:
				n-=1
		n = 0
		for x in range(i):
			if cnt[x] == cnt[-1]:
				n+=1
				cnt[x]=cnt[-1]
		return n
	else:
		for i in range(len(cnt)//2):
			# if cnt[i] != cnt[-1]:
			# 	cnt[i] = cnt[-1]
			# 	break
			if cnt[-1] != cnt[-1-i]:
				cnt[-1-i]=cnt[-1]
				break
			else: return 0
		n = len(cnt)-1
		while is_palindrome