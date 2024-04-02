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
    
	Include these tokens in the code: def is _ v owel ( ch : str )
	"""

    # Choose the following letters for checking vowel:
    vowels = {"A", "E", "I", "O", "U"}

    word = word.upper()
    
    index = len(word) - 1
    last_vowel_position = -1
    
    curr_letter = word[index]

    while index >= 0:
        if curr_letter in vowels:
            last_vowel_position = index

        curr_letter = word[index]
        
        index = index - 1

    if last_vowel_position != -1:
        index = last_vowel_position - 1
    
        while index >= 0:
            curr_letter = word[index]

            if curr_letter.isalpha():
                return curr_letter
            else:
                index = index - 1

    return ""


# Pybites solution 

def get_closest_vowel2(word):
    """Your task is to find the closest vowel that stands between 
    two consonants from the right side of the word (case sensitive).
    
    Vowses in the beginning and ending doesn't count. Return empty string if you didn't
    find any vowel met the above condition. 

    You may assume that the given string contains English letter only.

    Example:
    get_closest_vowel("yogurt") ==> "u"
    get_closest_vowel("FULL") ==> "U"
    get_closest_vowel("quick") ==> ""
    get_closest_vowel("ab") ==> ""
    """  

    vowels = "AEIOU"

    for i in range(len(word), -1, -1):
        if word[i].upper() in vowels and word[i-1].isalpha() and word[i+1].isalpha():
            return word[i]
    return ""

