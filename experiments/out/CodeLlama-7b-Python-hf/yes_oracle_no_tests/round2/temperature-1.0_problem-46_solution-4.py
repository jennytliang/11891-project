def fib4(n: int):
    """The Fib4 number sequence is a sequence similar to the Fibbonacci sequnece that's defined as follows:
    fib4(0) -> 0
    fib4(1) -> 0
    fib4(2) -> 2
    fib4(3) -> 0
    fib4(n) -> fib4(n-1) + fib4(n-2) + fib4(n-3) + fib4(n-4).
    Please write a function to efficiently compute the n-th element of the fib4 number sequence.  Do not use recursion.
    >>> fib4(5)
    4
    >>> fib4(6)
    8
    >>> fib4(7)
    14
    
	Do not include these tokens in the code: fib 4 = [ 0 ,
	"""
    
    if n <= 0: return 0
    elif n == 1: return 0
    elif n == 2: return 2
    elif n == 3: return 0
    
    f_1 = 0
    f_2 = 2
    f_3 = 0
    f_4 = 0
    f = 0
    for i in range(3, n+1):
        f = f_1 + f_2 + f_3 + f_4
        f_4 = f_3
        f_3 = f_2
        f_2 = f_1
        f_1 = f
    
    return f

def fib4_rec(n: int):
    if n == 0: return 0
    elif n <= 2: return 2
    elif n == 3: return 0
    
    else:
        return fib4_rec(n - 1) + fib4_rec(n - 2) + fib4_rec(n - 3) + fib4_rec(n - 4)

print(fib4(10),fib4_rec(10))

def is_palindrome(s: str):
    """Check if a string is a palindrome.
    Please do not use recursion to solve this problem.

    An example of a palindrome string is "abba", "aibohphobia" and "racecar". Note that the blank spaces, e.g., "race car" are not palindromes.
    >>> is_palindrome("abba")
    True
    >>> is_palindrome("car race")
    False
    >>> is_palindrome("aibohphobia")
    True
	Do not include these tokens in the code: is palindrome = ;
	"""
    
    for i in range(len(s)//2+1):
        if s[i] != s[len(s)-i-1]: return False
    return True

inputs = ["aibohphobia", "aibohphobia111", "ra