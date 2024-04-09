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
    
	Do not include these tokens in the code: # # This is my first solution
	"""
    words = sentence.split(' ')
    prime_words = []
    for word in words:
        if len(word) == 2:
            if word[0] in 'aeiou':
                prime_words.append(word)
            elif word[1] in 'aeiou':
                prime_words.append(word)
        elif len(word) == 3:
            if word[0] in 'aeiou':
                prime_words.append(word)
            elif word[1] in 'aeiou':
                prime_words.append(word)
            elif word[2] in 'aeiou':
                prime_words.append(word)
        elif len(word) == 4:
            if word[0] in 'aeiou':
                prime_words.append(word)
            elif word[1] in 'aeiou':
                prime_words.append(word)
            elif word[2] in 'aeiou':
                prime_words.append(word)
            elif word[3] in 'aeiou':
                prime_words.append(word)
        elif len(word) == 5:
            if word[0] in 'aeiou':
                prime_words.append(word)
            elif word[1] in 'aeiou':
                prime_words.append(word)
            elif word[2] in 'aeiou':
                prime_words.append(word)
            elif word[3] in 'aeiou':
                prime_words.append(word)
            elif word[4] in 'aeiou':
                prime_words.append(word)
        elif len(word) == 6:
            if word[0] in 'aeiou':
                prime_words.append(word)
            elif word[1] in 'aeiou':
                prime_words.append(word)
            elif word[2] in 'aeiou':
                prime_words.append(word)
            elif word[3] in 'aeiou':
                prime_words.append(word)
            elif word[4] in '