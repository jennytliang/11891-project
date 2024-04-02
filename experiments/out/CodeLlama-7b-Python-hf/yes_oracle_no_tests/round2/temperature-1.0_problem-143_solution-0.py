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
    
	Include these tokens in the code: is _ prime
	Do not include these tokens in the code: check Pr ime Number
	"""



    ### A2 - solution only
    """
    import math

    def is_prime(n):
        if n < 2:
            return False
        i = 2
        while i * i <= n:
            if n % i == 0:
                return False
    else:
        return True
 
    
    def words_in_sentence(sentence):
        answer = ''
        for word in sentence.split():
            if is_prime(len(word)) and word not in answer:
                answer += word + ' '
        return answer
    """
    
    
    
    ### A3 - final solution    
    def is_prime(n):
        if (n < 2):
            return False
        elif (n > 2 and n%2==0):
            return False
        else:
            i = 3
            while i * i <= n:
                if (n%i == 0):
                    return False
                i+=1		
            else:
                return True
    
    def words_in_sentence(sentence):
        return ' '.join(filter( lambda x: is_prime(len(x)) , sentense.split()))    
        
        
        
        
        
        