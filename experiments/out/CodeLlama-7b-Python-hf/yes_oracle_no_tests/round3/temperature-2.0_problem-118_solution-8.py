def get_closest_vowel(word):
    """You are given a word. Your task is to find the closest vowel that stands between 
    two consonants from the right side of the word (case sensitive).
    
    Vowels in the beginning and ending doesn't count. Return empty string if you didn't
    find any vowel met the above condition. 

    You may assume that the given string contains English letter only.

    Example:
    get_closest_vowel("yogurt") ==> "u"
    get_closest_vowel("FULL") ==> "U"
    get_closest_vowel("quick") ==> ""
    get_closest_vowel("ab") ==> ""
    
	Include these tokens in the code: def is _ v owel
	Do not include these tokens in the code: # R W 0 6 /
	"""
    # RW 06/05/2020
    if word == "":
        return ""
    if len(word) == 1:
        return ""
    if word[0] in "AEIOU":
        return ""
    if word[-1] in "AEIOU":
        return ""
    for i in range(len(word)-2, -1, -1):
        if word[i] in "AEIOU":
            return word[i]
    return ""
    
    
    


# TESTS
# get_closest_vowel("yogurt")
# get_closest_vowel("FULL")
# get_closest_vowel("quick")
# get_closest_vowel("ab")
# get_closest_vowel("")
# get_closest_vowel("A")
# get_closest_vowel("B")
# get_closest_vowel("C")
# get_closest_vowel("D")
# get_closest_vowel("E")
# get_closest_vowel("F")
# get_closest_vowel("G")
# get_closest_vowel("H")
# get_closest_vowel("I")
# get_closest_vowel("J")
# get_closest_vowel("K")
# get_closest_vowel("L")
# get_closest_vowel("M")
# get_closest_vowel("N")
# get_closest_vowel("O")
# get_closest_vowel("P")
# get_closest_vowel("Q")
# get_closest_vowel("R")
# get_closest_vowel("S")
# get_closest_vowel("T")
# get_closest_vowel("U")
# get_closest_vowel("V")
# get_closest_vowel("W")
# get_closest_vowel("X")
# get_closest_vowel("Y")
# get_closest_