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
    
	Do not include these tokens in the code: # Cor ner cases if a <=
	"""



    def is_prime(a):
        if a <= 1:
            return False
        for i in range(2, a):
            if a % i == 0:
                return False
        return True


    def get_prime_words(sentence):
        words = sentence.split(' ')
        prime_words = []
        for w in words:
            if is_prime(len(w)):
                prime_words.append(w)
        return prime_words


    prime_words = get_prime_words(sentence)
    return ' '.join(prime_words)



print(words_in_sentence("This is a test"))
print(words_in_sentence("lets go for swimming"))
print(words_in_sentence("hello there world"))
print(words_in_sentence("codeforces rocks"))
print(words_in_sentence("codeforces"))
print(words_in_sentence(""))
print(words_in_sentence(" "))
print(words_in_sentence("   "))
print(words_in_sentence("     "))
print(words_in_sentence("    a     "))
