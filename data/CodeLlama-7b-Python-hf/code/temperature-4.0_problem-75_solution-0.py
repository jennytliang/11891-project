def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """

    p = a
    p1=2
    p2=5

    if a < 2:
       print("Number is a prime number")

    while p:
      for x in range(100):
         p2 = p2+2 
         if a ==  p1*p2:
            if is_prime( p1 )  or is_prime( p2):
             print(" Number is a multiple prime number ");
             return ( p==1 )
            break

      p1 = p1+2



