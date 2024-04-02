def tri(n):
    """Everyone knows Fibonacci sequence, it was studied deeply by mathematicians in 
    the last couple centuries. However, what people don't know is Tribonacci sequence.
    Tribonacci sequence is defined by the recurrence:
    tri(1) = 3
    tri(n) = 1 + n / 2, if n is even.
    tri(n) =  tri(n - 1) + tri(n - 2) + tri(n + 1), if n is odd.
    For example:
    tri(2) = 1 + (2 / 2) = 2
    tri(4) = 3
    tri(3) = tri(2) + tri(1) + tri(4)
           = 2 + 3 + 3 = 8 
    You are given a non-negative integer number n, you have to a return a list of the 
    first n + 1 numbers of the Tribonacci sequence.
    Examples:
    tri(3) = [1, 3, 2, 8]
    
	Include these tokens in the code: if n ==
	"""
    def tri(n):
        result = [1,1]
        if n == 0:
            return []
        if n == 1:
            return [1]
        if n == 2:
            return [1,1]
        for i in range(3,n+1):
            result.append(result[i-1]+result[i-2]+result[i-3])
        return result
    return tri(n)

#print tri(3)
#[1, 3, 2, 8]

def is_prime(n):
    """Given a number n, determine if it's prime.
    The input n is always a positive integer.
    Examples:
    is_prime(12) = False
    is_prime(2) = True
    is_prime(561) = True
    is_prime(31) = True
    is_prime(45) = False
    
    Include these tokens in the code: if n ==
    """
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

#print is_prime(12)
#False
#print is_prime(2)
#True
#print is_prime(561)
#True
#print is_prime(31)
#True
#print is_prime(45)
#False

def is_palindrome(s):
    """Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.
    Note: For the purpose of this problem, we define empty string as valid palindrome.
    Examples:
    is_palindrome("A man, a plan, a canal: Panama") = True
    is_palindrome("hello") = False
    is_palindrome("") = True
    
    Include these tokens in the code: if s ==
    """
    s = s.lower().replace(" ", "")
    if s == s[::-1]:
