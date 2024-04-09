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
    
	Include these tokens in the code: not ( a <
	Do not include these tokens in the code: >
	"""

    
    def is_prime(a):
    	if a < 2:
    		return False
    	for i in range(2, a):
    		if a % i == 0:
    			return False
    	return True
    
    def find_primes(a):
    	primes = []
    	for i in range(len(a)):
    		if is_prime(len(a[i])):
    			primes.append(a[i])
    	return primes
    
    def get_words(a):
    	words = []
    	for i in range(len(a)):
    		if a[i] != " ":
    			words.append(a[i])
    		else:
    			words.append(" ")
    	return words
    
    def get_word_list(a):
    	word_list = []
    	for i in range(len(a)):
    		if a[i] != " ":
    			word_list.append(a[i])
    		else:
    			word_list.append(" ")
    	return word_list
    
    def get_word_list_2(a):
    	word_list = []
    	for i in range(len(a)):
    		if a[i] != " ":
    			word_list.append(a[i])
    		else:
    			word_list.append(" ")
    	return word_list
    
    def get_words_2(a):
    	words = []
    	for i in range(len(a)):
    		if a[i] != " ":
    			words.append(a[i])
    		else:
    			words.append(" ")
    	return words
    
    def get_words_3(a):
    	words = []
    	for i in range(len(a)):
    		if a[i] != " ":
    			words.append(a[i])
    		