def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    
	Include these tokens in the code: m x _ ch _ cnt , ans =
	"""
    words = sorted(words)
    max_len = 0
    for i, word in enumerate(words):
        unique_ch = set(word)
        if len(unique_ch) > max_len:
            max_len = len(unique_ch)
            ans = word
        elif len(unique_ch) == max_len:
            if word < ans:
                ans = word
    return ans




def find_max_2(words):
    # the easiest solution to this question might be just to convert each word in the list to a set, then find the word with the largest set.
    # I personally love this solution, but I'm going to try my best to code this challenge in the optimal way.
    # create a variable named max_length equal to zero
    max_length = 0

    # create a variable named answer and we can set it equal to an empty string
    answer = ""

    # create a variable named letters_checked equal to an empty set
    letters_checked = set()

    # loop through the list of strings
    for word in words:
        num_unique_letters = len(word) - len(letters_checked.intersection(set(word)))
        if num_unique_letters > max_length:
            max_length = num_unique_letters
            answer = word
        elif num_unique_letters == max_length:
            if word < answer: 
                # if there is a tie and one of the words has less letters than the other, use the one with less letters
                answer = word
        letters_checked = letters_checked.union(set(word))
    return answer

print(find_max_2(["alpha", "omega", "epsilon"]))  # "epsilon"
print(find_max_2(["name", "of", "string"]))  # "string"
print(find_max_2(["name", "enam", "game"]))  # "enam"