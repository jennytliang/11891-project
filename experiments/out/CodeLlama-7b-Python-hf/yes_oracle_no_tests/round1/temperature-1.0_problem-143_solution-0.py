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
    
	Include these tokens in the code: def is _ prime ( a ): return
	"""


    def checkPrimeNumber(numb):
        if numb == 1:
            return False,
        elif numb in [2,3,5,7]:
            return True, numb
        else:
            for i in range(2, int(numb**1/2)+1):
                if numb%i==0:
                    return False
        return True
	
	def get_words(sentence):
        
	   return [word.strip() for word in sentence.split(' ')]


    def getPrimeNumber(w, n):
        l_word = (len(w)**2)//2
        if l_word > n:
            l_word = n
        str_num = f'{w}{l_word}'
        if 'len(str_num)' % 2 != 0:
            str_num += '0'
        print(str_num, l_word)
        checkPrime, num = checkPrimeNumber(l_word)
        if checkPrime==True: 
            return w
        return ""
    
    result=""
    sentence = sentence.split()
    for i in sentence:
        result += getPrimeNumber(i,len(i)) + " "
        print(result)
    return result
