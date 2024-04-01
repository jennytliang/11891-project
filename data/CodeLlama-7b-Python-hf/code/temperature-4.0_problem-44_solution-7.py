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
    """

    if x<0 or base<=0:
        raise Exception("base needs to be base numbers are "
                        "great than zero and the value must be a non-negative integer.")

    if x//base != 0:  # x//base always >= 0.
        raise Exception("this is the example for this method. "
                          "you need to implement the core logic first")
    digits='0123456789ABCDEFGHIJ'
    str_x = ""
    while x>=1:
        x, r = divmod(x, base -1)    # r=x%base or r=  x- base*(x/base)    # base=3 => -1 % -2 is illegal
        r+=base      # r= base
        # str_x+= str(r%base)        # str(9 %3)= str(0)= '0', we want 1 to show up so + base=2+base=base+2, then str(2)=02.
        r=digits[r]   # str_x+= digits[i], this gives us A=10=> 'A', G=7=>'G' instead of 1,6 => 1/0=0,6-1=5,6/(1-1)=0,5%base is -1. we do +base so 1 and 5 both will be 6 because we add +base to them so that we dont have 16=>2 but +base is base so thats +1.
        str_x+= r     # str+=digits[i]: gives us A(G)= 'A'(G)= ABCDG, ABCDEF...
    else:
        return str_x