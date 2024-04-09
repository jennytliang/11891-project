def will_it_fly(q,w):
    '''
    Write a function that returns True if the object q will fly, and False otherwise.
    The object q will fly if it's balanced (it is a palindromic list) and the sum of its elements is less than or equal the maximum possible weight w.

    Example:
    will_it_fly([1, 2], 5) ➞ False 
    # 1+2 is less than the maximum possible weight, but it's unbalanced.

    will_it_fly([3, 2, 3], 1) ➞ False
    # it's balanced, but 3+2+3 is more than the maximum possible weight.

    will_it_fly([3, 2, 3], 9) ➞ True
    # 3+2+3 is less than the maximum possible weight, and it's balanced.

    will_it_fly([3], 5) ➞ True
    # 3 is less than the maximum possible weight, and it's balanced.
    
	'''

    
    return q == q[::-1] and su(q) <= w




def su(q):
    '''
    Write a function that takes a list of integers and returns the sum of the integers.

    Example:
    su([2, 3, 3, 2]) ➞ 11

    su([3, 1, 4, 1, 5, 9]) ➞ 22

    su([1]) ➞ 1
    '''
    
    return sum(q)




def is_palindrome(s):
    '''
    Write a function that takes a string and returns True if the letters in the string form a palindrome, and False otherwise.

    Examples
    is_palindrome("racecar") ➞ True
    is_palindrome("radar") ➞ True
    is_palindrome("mom") ➞ True
    is_palindrome("cat") ➞ False
    is_palindrome("civic") ➞ True
    is_palindrome("level") ➞ False
    is_palindrome("a") ➞ True
    is_palindrome("") ➞ True
    is_palindrome(" ") ➞ True
    is_palindrome("1234554321") ➞ True
    is_palindrome("123455432") ➞ False
    is_palindrome("12345") ➞ False
    is_palindrome("12345543211") ➞ False
    is_palindrome("123455432111") ➞ False
    is_palindrome("1234554321111") ➞ False
    '''
    
    return s == s[::-1]




def is_palindrome_two(s):
    '''
    Write a function that takes a string and returns True if the letters