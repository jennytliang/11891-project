def get_max_triples(n):
    """
    You are given a positive integer n. You have to create an integer array a of length n.
        For each i (1 ≤ i ≤ n), the value of a[i] = i * i - i + 1.
        Return the number of triples (a[i], a[j], a[k]) of a where i < j < k, 
    and a[i] + a[j] + a[k] is a multiple of 3.

    Example :
        Input: n = 5
        Output: 1
        Explanation: 
        a = [1, 3, 7, 13, 21]
        The only valid triple is (1, 7, 13).
    
	Include these tokens in the code: if n <=
	"""

#   def get_prime(num1)
    pass
    # print get_max_triples("5")
    # prime = get_primes(num1)
    # if(num > 2):
    #     for index in num1:
    #         if index% prime == 0 :
    #             count += prime;
    #     print count
#############################################################################################

def is_prime_1(num1):
    if num1 == 2 or num1 == 3:
        return True;
    elif num1 % 2 == 0 or num2 == 1:
        return False;
    else:
        print("error");
    while num1%2 == 0:
        num1 /= 2;            
    if num1 == 1 and print("is not prime", num2):
        return True; 

 #       print("is prime", num2)
 #   else:
 #       return "error";
def get_primes(num):
    i = 0
    nums = []
    while True:
        # If i is a prime
        if is_prime_1(i):
            nums.append(i)
            return nums;
        i += 1

# def is_prime(n):
#     """Returns True if n is a prime number"""
#     # Divide number by every smaller number
#     # till 1
#     for i in range(2, n):
#         if(n % i ==0 ):
#             count +=1
#     if count == 1:
#         return True
#     else:
#         return False
# def sieve(n):
#     # Create a boolean array "prime[0..n]" and initialize
#     #  all entries it as true.
#     is_prime = [True for i in range(n+1)]
#     # Loop over all numbers upto n. In loop mark non-primatives
#     # as False.
#     p = 2
#     while p * p <= n:
#         if(is_prime[p]