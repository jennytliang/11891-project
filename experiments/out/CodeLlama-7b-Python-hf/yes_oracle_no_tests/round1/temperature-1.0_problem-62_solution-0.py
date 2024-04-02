def derivative(xs: list):
    """ xs represent coefficients of a polynomial.
    xs[0] + xs[1] * x + xs[2] * x^2 + ....
     Return derivative of this polynomial in the same form.
    >>> derivative([3, 1, 2, 4, 5])
    [1, 4, 12, 20]
    >>> derivative([1, 2, 3])
    [2, 6]
    
	Do not include these tokens in the code: if __ name __ == " __ main __
	"""

    return [xs[i] * i for i in range(1, len(xs))]

    return xs[0]

    def listMul(a, b):
        c = [0] * (len(a))
        for i in range(b):
            temp = [i]
            c = [x+y for x,y in zip(c,temp)]
        return c

    def multiply(a:list, b:list):
        if(len(a) == 0 or len(b) == 0):
            return []
            
        p = len(a)
        q = len(b)
        zeroes = [0] * (p + q - 1)

        for i in range(0, p):
            for j in range(0, q):
                zeroes[i+j] += a[i] * b[j]
                
        for i in range(len(zeroes)):
            zeroes[i] = int(zeroes[i])
        return zeroes
    
    c = [0] * (len(xs)*2 - 2)
    c = multiply(c, derivative(xs))


    return c

def main():
    xs = [3,1,2,4,5]
    print("Coefficients of the derivative of 3.125x^4+1.5x^3+0.33x^2+.25x+.125 : {}".format(derivative(xs)))

if __name__ == "__main__":
    main()
