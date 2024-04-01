def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """

    primes_list = [2, 3]
    for i in range(1, 6001):
        is_prim = 1
        for j in range(2, i):
            if i % j == 0:
                is_prim = 0
                break
        if is_prim:
            primes_list.append(i)
    word = ''
    word = string
    for i in word:
        count_word = 1
        for j in word:
            if i != j:
                count_word += 1
    print(primes_list[-1])