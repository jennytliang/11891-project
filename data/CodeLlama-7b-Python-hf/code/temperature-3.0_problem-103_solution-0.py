def rounded_avg(n, m):
    """You are given two positive integers n and m, and your task is to compute the
    average of the integers from n through m (including n and m). 
    Round the answer to the nearest integer and convert that to binary.
    If n is greater than m, return -1.
    Example:
    rounded_avg(1, 5) => "0b11"
    rounded_avg(7, 5) => -1
    rounded_avg(10, 20) => "0b1111"
    rounded_avg(20, 33) => "0b11010"
    """
    pass





"""
    def dec_to_bin(n):
        result = []
        while n > 0:
            result.append(str(n%2))
            n //= 2
        return ''.join(result[::-1])

    def rounded_avg(n, m):
        if m <= n:
            return -1
        avg = (n + m)//2
        b = dec_to_bin(avg)
        return '0b' + ''.join(b[:-1] + [str(int(b[-1])+int(b[-1]=='1'))])
"""
