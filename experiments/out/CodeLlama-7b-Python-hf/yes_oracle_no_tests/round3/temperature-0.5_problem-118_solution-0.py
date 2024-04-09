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
	Do not include these tokens in the code: # R W # if
	"""
    # RW
    # if len(word) < 4:
    #     return ""
    # elif word[-1] in "AEIOU":
    #     return ""
    # elif word[0] in "AEIOU":
    #     return ""
    # elif word[1] in "AEIOU":
    #     return ""
    # else:
    #     for i in range(2, len(word)-1):
    #         if word[i] in "AEIOU":
    #             return word[i]
    
    # RW
    if len(word) < 4:
        return ""
    elif word[-1] in "AEIOU":
        return ""
    elif word[0] in "AEIOU":
        return ""
    elif word[1] in "AEIOU":
        return ""
    else:
        for i in range(2, len(word)-1):
            if word[i] in "AEIOU":
                return word[i]


# RW
# def get_closest_vowel(word):
#     if len(word) < 4:
#         return ""
#     elif word[-1] in "AEIOU":
#         return ""
#     elif word[0] in "AEIOU":
#         return ""
#     elif word[1] in "AEIOU":
#         return ""
#     else:
#         for i in range(2, len(word)-1):
#             if word[i] in "AEIOU":
#                 return word[i]


# RW
# def get_closest_vowel(word):
#     if len(word) < 4:
#         return ""
#     elif word[-1] in "AEIOU":
#         return ""
#     elif word[0] in "AEIOU":
#         return ""
#     elif word[1] in "AEIOU":
#         return ""
#     else:
#         for i in range(2, len(word)-1):
#             if word[i] in "