def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """

    is_prime = "True"
    check_prime = True 
    primes = []

    if a >= 1000: 
      return "False"
    elif  a < 100: 
      return "Not implemented"
    elif a % 100 >= 20 or a % 2 ==  0:
      return "Not possible"
    elif  a <=  5 * 5 * 6:
      prime_1 = 2 
      prime_6 = 5 # 3 * 5 
      prime__1 = prime_6 - 1  #3 * 5 = 
      mult_3prime = 20  # 10 * 2 (20) = 200
      
      
      if(a % prime_1 % 10 == 0 or a % prime__1 % 10 ==0):
          is_prime = not check_prime
          return "not possible"
      elif (   a == prime_1 * 2 * 2 or  a == prime__1 * 3 * 2):
          return "not possible" 
      elif ( a ==  prime_6 * 3):
          return "possible with one pair of prime numbers " 
   
      

    else: 
      for i in range (11, a - 1, 2): # only odd number from the sqrt root number -1 

          if( a % i ==  0):
             check_prime = False 

          if check_prime:

            print(i)

            is_prime[i % 10 ] = check_prime 
            primes[] 
    
      for p in primes : 

          if int(a / 3) % x == 0 == x % 10




import numpy as np

def is_floats(x) -> bool:
    # check if it is float; List[float]; Tuple[float]
    if isinstance(x, float):
        return True
    if isinstance(x, (list, tuple)):
        return all(isinstance(i, float) for i in x)
    if isinstance(x, np.ndarray):
        return x.dtype == np.float64 or x.dtype == np.float32
    return False


def assertion(out, exp, atol):
    exact_match = out == exp

    if atol == 0 and is_floats(exp):
        atol = 1e-6
    if not exact_match and atol != 0:
        np.testing.assert_allclose(out, exp, atol=atol)
    else:
        assert exact_match


def check(candidate):
    inputs = [[5], [30], [8], [10], [33], [49], [77], [91], [99], [6], [90], [98], [25], [21], [48], [20], [22], [32], [26], [78], [19], [47], [31], [29], [-98], [-37], [-38], [28], [18], [23], [-92], [-2], [57], [-99], [58], [56], [-1], [92], [1], [-80], [34], [-75], [-100], [-95], [16], [-94], [17], [59], [-7], [93], [-82], [-15], [-81], [-96], [-74], [2], [3], [7], [97], [42], [-101], [43], [44], [45], [-56], [60], [-55], [46], [62], [55], [61], [41], [40], [-57], [63], [-102], [52], [-72], [-97], [94], [12], [89], [53], [0], [64], [-58], [65], [-71], [95], [35], [-70], [96], [-59], [15], [-33]]
    results = [False, True, True, False, False, False, False, False, True, False, False, True, False, False, False, True, False, False, False, True, False, False, False, False, False, False, False, True, True, False, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, True, False, False, True, True, False, False, False, False, False, False, False, False, False, False, True, False, True, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
    for i, (inp, exp) in enumerate(zip(inputs, results)):
        assertion(candidate(*inp), exp, 0)


check(is_multiply_prime)