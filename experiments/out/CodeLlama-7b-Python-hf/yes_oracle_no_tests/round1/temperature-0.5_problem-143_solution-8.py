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
    
	Include these tokens in the code:  def is _ prime ( a ):
	Do not include these tokens in the code: # TODO : Write your code here
	"""

    # 1. Take in the input
    # 2. Create a list with words
    # 3. Create a list with prime numbers
    # 4. Create a function to check if number is prime
    # 5. Check if the length of the word is in the prime list
    # 6. If it is, add it to the new list
    # 7. Return the new list

    # Create a list with words
    words = sentence.split()

    # Create a list with prime numbers
    prime_numbers = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

    # Create a function to check if number is prime
    def is_prime(a):
        for i in range(2, int(a / 2) + 1):
            if a % i == 0:
                return False
        return True

    # Check if the length of the word is in the prime list
    new_list = []
    for word in words:
        if len(word) in prime_numbers:
            new_list.append(word)

    # Return the new list
    return " ".join(new_list)


# print(words_in_sentence("This is a test"))
# print(words_in_sentence("lets go for swimming"))
