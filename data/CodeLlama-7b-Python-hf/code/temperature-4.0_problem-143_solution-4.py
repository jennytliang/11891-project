def words_in_sentence(sentence):
    """
    You are given a string representing a sentence,
    the sentence contains some words separated by a space,
    and you have to return a string that contains the words from the original sentence,
    whose lengths are prime numbers,
    the order of the words in the new string should be the same as the original one.

    Example 1:
        Input: sentence = "This is a test"
        Output: "is"

    Example 2:
        Input: sentence = "lets go for swimming"
        Output: "go for"

    Constraints:
        * 1 <= len(sentence) <= 100
        * sentence contains only letters
    """
    primes = generate_primes([n for n in range(2,100010)])
    # words = [n for n in sentence.split(" ") if int(n) in prime_numbers]
    words = [w for w in sentence.split(' ') if w in primes] # faster!

    return ' '.join(words)

# Generating Primes Numbers
PRM = [0]*10100
def sieve(max_): # O(max_)
    ''' Returns prime numbers below n '''
    prime, primes= [1], [] # Init prime list for 0 <= i < 3 and primes list to keep them in prm array
    for num, isprime in enumerate(PRM):
        if num==0: PRM[primes[-1]] = 2
        elif num == 1: continue
        elif isprime:
            primes.append(prime.append(num)) and (num*num<=n and PRM[i-1]=2 for i in range(num+num, n+1, num)| n*n<99*num or n==2) or (p-1>=len(prime) and 
        return list(filter(None, prime[:-1], primes)

    return primes[-1]
            
    return list(np.append(np.delete(prime, len(prime)-1], primes))

    
