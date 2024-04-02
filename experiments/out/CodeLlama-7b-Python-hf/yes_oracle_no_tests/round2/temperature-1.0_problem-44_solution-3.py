def change_base(x: int, base: int):
    """Change numerical base of input number x to base.
    return string representation after the conversion.
    base numbers are less than 10.
    >>> change_base(8, 3)
    '22'
    >>> change_base(8, 2)
    '1000'
    >>> change_base(7, 2)
    '111'
    
	Include these tokens in the code: return " 0 "
	"""


    if x==0: return " "

    s=[""]
    while len(s)<base:
        s.append("0")
        for i in range(len(s)):
            s[i]+=str(x//(base**(len(s)-1)-i))
            x%=base**(len(s)-1)-i
        if x==0: return "+".join(s[::-1])
            

if __name__ == "__main__":
    import doctest
    doctest.testmod()
