def derivative(xs: list):
    """ xs represent coefficients of a polynomial.
    xs[0] + xs[1] * x + xs[2] * x^2 + ....
     Return derivative of this polynomial in the same form.
    >>> derivative([3, 1, 2, 4, 5])
    [1, 4, 12, 20]
    >>> derivative([1, 2, 3])
    [2, 6]
    """
    result = []  # Create a new empty list of coefficients for the result, called results.
    xpowers = [list(x ** x for x in range(0, 5))]
    pow = 1  # Define a variable holding the power for which we are currently computing values of x
    y = xs.copy()  # Define another variable y, holding an array of the xs
    y0 = 0

    while ((pow < len(xpowers[2])) and (y[0] == y0)):  # while power of x is smaller then the size of xs and first entry in xs is still the same we are still looking for a higher order derivative (x0 being constant)
        print("pow = ", pow, "y0 =", y0, "y[0] =", y[0])

        # add new list of x to power of n to the xpo[2](2) power list of all powers of x

        xlist = list(map((x(**pow)), (x ** x for x in range((pow + 1)))))
        #
        # for x(**pow,) in xlist)
        #     print("adding x to the pow list", xpowers0)
        #     newlist = list(y(**x) if (x < len(x)) else []
        ##
        # print("the new list of exponents for power ", pow, ":", xpower0)
        x = y[:] # get a new y, same length as the input y, but containing different values (0s) because the first 1 is not needed
        for i in range(pow,len(x) - 1): # we are starting from pow (so, for instance 2) until 4th element, in the xs example (the length of x from 1) so we have 3 (until i = 2 is included in the range so the for loop starts at index [2])
            #print("before adding coeff", x(**i))
            newlist.insert(x(**x) + list(a(x(**pow))*xpower0),) # add the ith element from x (coefficient) multiplied by all the list xpowers of powers of the first derivative from i, in this case: for 1, that is 1*x^4,1*x^42, etc etc
            #print("after adding", x(**(i))
            x(i=1,pow=pow) += newlist #[x(**x) + xpower0

        y[0] = newy  # update y the same as xs, adding a new element (0)
        result = x * 2
        pow += 1  # update power for the for loop as we are looking the next higher term

    for y in result:
        return newlist # return this result, with the higher order derivative
            #print(list(newlist[2]))

print('the new derivative is = ' + str((derivative([5, 5, 3])))
