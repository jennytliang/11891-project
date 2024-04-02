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
    
    
    def trinum(number):
        def next_tribin(curr): return (curr[0], curr[1], curr[2] + curr[0] + curr[1],)
        def tri(n):
            return [1, 1, 2] if n == 1 else tri(n - 1) if n >= 2 else ""
        n = tri(number)
        for num in range(3, number + 1):
            n = next_tribin(n)
        return n
    def trinum2(number):
        def next_tribin(curr): return (curr[0], curr[1], curr[2] + curr[0] + curr[1],)
        def tri(n): return [1, 1, 2] if n == 1 else tri(n - 1) if n >= 2 else ""
        def trihelp(n): return trinum(n)
        def trin(number):
            x = trinum(number)
            for i in range(3, number + 1):
                print(x)
                x = next_tribin(x)
        return trin(number)
    trinum2(2)
   