def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    
	Include these tokens in the code: even , odd =
	"""
    # BEGIN PROBLEM 1
    even = 0
    odd = 0
    for num in str(num):
        if int(num) % 2 == 0:
            even += 1
        else:
            odd += 1
    return even, odd
    # END PROBLEM 1


def all_same_letter(string):
    """Given a string. return True if every character is the same.

    Example:
        all_same_letter("a") ==> True
        all_same_letter("abc") ==> False
    
    Note: string can only contain lowercase letters.
    """
    # BEGIN PROBLEM 2
    first = string[0]
    for letter in string:
        if letter != first:
            return False
    return True
    # END PROBLEM 2


def pig_latin(word):
    """Return the given word in Pig Latin.

    Pig Latin is a game of alterations played on the English language game.
    To create the Pig Latin form of an English word the initial consonant 
    sound is transposed to the end of the word and an ay is affixed 
    (Ex.: "banana" would yield anana-bay). Read Wikipedia for more details.
    If the word begins with a vowel append way to the word (Ex.: "algorithm"
    would yield algorithm-way).
    """
    # BEGIN PROBLEM 3
    if word[0] in 'aeiou':
        return word + 'way'
    else:
        for letter in word:
            if letter in 'aeiou':
                return word[word.index(letter):] + '-' + word[:word.index(letter)] + 'ay'
    # END PROBLEM 3


def vowel_indices(word):
    """Return a list of all vowel indices in the given word.

    Example:
        vowel_indices('banana') ==> [1, 3, 4]
    """
    # BEGIN PROBLEM 4
    vowels = '