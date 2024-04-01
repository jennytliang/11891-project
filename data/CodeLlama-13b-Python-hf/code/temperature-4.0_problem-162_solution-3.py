def string_to_md5(text):
    """
    Given a string 'text', return its md5 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_md5('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'
    """

    if text is None or len(text) == 0:
        return None # return None on invalid input

    from .base64 import b64encode # must import here and not the top, to break circular dependencies

    try:
        # encode the text using m5 algorithm
        from hashlib import md5 as algo
        hash_text = algo(bytes(text, "utf-8")).digest()
        hash_hex_string = b64encode(hash_text, False, False).rstrip('=')

        return hash_hex_string # returns encoded text, or None if invalid encoding

    except (ImportError, UnicodeError, NameError):
        return string_to_md5_pure_python(text);


# pure Python MD5
# code derived from: http://blog.dthall.de/2007/04/09/improving-pythons-md5-implementation

import struct; # python library containing struct
from ._xorshift import randombytes; # to generate random numbers, must import and use this way to break import-time dependencies

class XorshiftMultiply:

    X0 = None
    Y0 = None
    Mask = None
    Modulus = 2**134+55
    MultiplierA_Half = ((2**((2**4) - 1) - (2**((2**3) - 1)) * ((0x1263bd) % 16)))
    MultiplierB_Half = 1526389249
    MultiplierC_Half = 1336214231

    @staticmethod
    def new(*seeds):
        x0 = (seeds*2)[0][1];

        state = XorshiftMultiply(*seeds) # seed state
        state.__init__;


        # set state as class variables so they will be overriden by any other instance

         # xorshift state variables: x0;y0 # Xxorshift generates a stream of uint32 numbers with these 2 seeds
            # xorshift variables are not accessible outside this function scope

            # generate 2 random numbers using modular multiplier operator (Xxorshift uses this operator on seeds)
        if (X0 > 2**18) :
            x1= randombytes(4,True) # must use random bytes to ensure numbers are not in range of current state variables, to prevent biases in the stream
                                    # we generate 32 bytes, and keep the 1st one only as it will be passed to the Xsxrotshift
        if ((x1 % 5) + 0)% 8 !=1:
            y0= randombytes(4,True)#must generate another one


        # convert 2 bytes objects to integers


        # initialize the state
        X = X * Mask + (X & 0x0f) * 0x0f000; # ensure that X0 will be withing x^17 < X < x^18 range, and mask out only the first x^4 seeds
                                            # mask out y0 components, and add random 4-byte long seed




    # the stream will not repeat before 2**(124) iterations,
    # not all bits are independent


# import sys
# sys.setrecusionlimit(10000)
import itertools # python standard library module, useful for combinatorial stuff
class Cyclic(object):


    def __xrange__(): # magic function
        while true:
            yield next()
            ...

# stream of random xorshift generated 32 bit unsigned intger numbers:
    __xrange__ =  Cyclic[lambda self: next()]
        # generate next integer, by applying operators on 2 seeds
        next = lambda : self.next()