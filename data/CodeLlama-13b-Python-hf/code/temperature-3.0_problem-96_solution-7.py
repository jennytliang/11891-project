def count_up_to(n):
    """Implement a function that takes an non-negative integer and returns an array of the first n
    integers that are prime numbers and less than n.
    for example:
    count_up_to(5) => [2,3]
    count_up_to(11) => [2,3,5,7]
    count_up_to(0) => []
    count_up_to(20) => [2,3,5,7,11,13,17,19]
    count_up_to(1) => []
    count_up_to(18) => [2,3,5,7,11,13,17]
    """

    prime_numbers = []
    for x in range(2,n):
        prime = True
        for y in range(2,x): 
            if x % y == 0:
                prime = False
                break
        if prime:
            prime_numbers.append(x)
    
    return prime_numbers 