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
    
	Do not include these tokens in the code: if a == 1 :
	"""


    def is_prime(a):
 
        # Corner cases
        if a <= 1:
            return False
        if a == 2:
            return True
 
        # This is checked so that we can skip
        # middle five numbers in below loop
        if a % 2 == 0:
            return False
 
        # Loop's division is optimized
        for i in range(3, int(a**0.5)+1, 2):
            if a % i == 0:
                return False
 
        return True
 
    # Main code
    lst = [i for i in sentence.split(" ") if is_prime(len(i))]
    return " ".join(lst)


# Test cases:
print(words_in_sentence("This is a test") == "is")
print(words_in_sentence("lets go for swimming") == "go for")
print(words_in_sentence("a a aa aaa aaaa") == "")
print(words_in_sentence("") == "")
print(words_in_sentence("a aa a a") == "a")
print(words_in_sentence("a aa a a a") == "a")
print(words_in_sentence("a aa a a a a") == "a")
print(words_in_sentence("a aa a a a a a") == "a")
print(words_in_sentence("a aa a a a a a a") == "aa")
print(words_in_sentence("a aa a a a a a a a") == "aa")
print(words_in_sentence("a aa a a a a a a a a") == "aa")
print(words_in_sentence("a aa a a a a a a a a a") == "aa")
print(words_in_sentence("a aa a a a a a a a a a a") == "aa")
print(words_in_sentence("a aa a a a a a a a a a a a") == "aa")
print(words_in_sentence("a aa a a a a a a a a a a a a")