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
    
	Include these tokens in the code: def
	Do not include these tokens in the code: # Take advantage of the fact that
	"""
    # pass
    # R1
    # vowel = "aeiou"
    # closest_vowel = ""
    # for i in range(len(word)-1,0,-1):
    #     if word[i] in vowel and word[i-1] in vowel:
    #         closest_vowel = word[i]
    #         break
    # return closest_vowel
    # R2
    # vowel = "aeiou"
    # closest_vowel = ""
    # for i in range(len(word)-1,0,-1):
    #     if word[i] in vowel and word[i-1] not in vowel:
    #         closest_vowel = word[i]
    #         break
    # return closest_vowel
    # R3
    # vowel = "aeiou"
    # closest_vowel = ""
    # for i in range(len(word)-1,0,-1):
    #     if word[i] not in vowel and word[i-1] in vowel:
    #         closest_vowel = word[i]
    #         break
    # return closest_vowel
    # R4
    # vowel = "aeiou"
    # closest_vowel = ""
    # for i in range(len(word)-1,0,-1):
    #     if word[i] not in vowel and word[i-1] not in vowel:
    #         closest_vowel = word[i]
    #         break
    # return closest_vowel
    # R5
    # vowel = "aeiou"
    # closest_vowel = ""
    # for i in range(len(word)-1,0,-1):
    #     if word[i] in vowel and word[i-1] not in vowel:
    #         closest_vowel = word[i]
    #         break
    # return closest_vowel
    # R6
    # vowel = "aeiou"
    # closest_vowel = ""
    # for i in range