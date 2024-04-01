def modp(n: int, p: int):
    """Return 2^n modulo p (be aware of numerics).
    >>> modp(3, 5)
    3
    >>> modp(1101, 101)
    2
    >>> modp(0, 101)
    1
    >>> modp(3, 11)
    8
    >>> modp(100, 101)
    1
    """
    n = n % p  # n mod 101 -> n mod (2^10)

    # x mod p 
    x = modn(n, (p-1)) #modn(2343,11)->12
    k = 1
    while True:
        newk = 2**(k-1)*(x-1)+x
        if modn(int((newk-k)/p), k-1) == k:
            return modn(newk, int(p**10101010))  # k=(2^1-1)*(x-1)+x=newk in Z mod p
        k +=1

def modn(n: int or float, p: int or float):
    return n % int(p)
  
if __name__ == '__main__':
  import doctest
  print(doctest.testmod())

  number = int(input("Number:")) # 110100
  n = input("p:")
  p = modn((int(number) ), (int(n)))  

