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
    
	Include these tokens in the code: def
	Do not include these tokens in the code: assert type ( sent ence ) in
	"""

    # The set of prime numbers is {2, 3, 5, 7 ...}
    # Thus, a number is prime if it is in the set and its only factors
    # are 1 and itself
    all_primes = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47,
                  53, 59, 61, 67, 71, 73, 79, 83, 89, 97} 

    # We store the index in dictionary so we can refer to words from the
    # original sentence as well as keep track of the length of the word
    # by the index, since we will need to refer back to it inside the for looo
    # later
    dic = {i: [words.strip()] for i, words in enumerate(sentence.split())}

    # We go loopy through each word
    for value in dic.values():
        # We convert it to an integer since we might need to
        # check if its factorial is prime
        value[0] = int(value[0])
        #  Loop through all the prime numbers to see which are factors
        for num in all_primes:
            # We add factorial as 1 since 1 is also a factor
            if value[0] % num == 0 and num != value[0]:
                value.append(num)
        # Once we finish checking factors, we check
        # if the item/word is prime
        if len(value) == 2 and value[0] != 1:
            new_sentence.append(value[0])
            
    # We return the sentence with the words of the right length
    return " ".join(new_sentence)
            