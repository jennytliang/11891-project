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
    
	Include these tokens in the code: def is
	Do not include these tokens in the code: v ow els = [" a ",
	"""
    # Your code goes here
    vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
    word = word.split()
    for j in range(len(word)-1, 0, -1):
        for i in range(len(word[j])-1, 0, -1):
            if word[j][i] == " ":
                continue
            if word[j][i] in vowels:
                if i == 0:
                    if j == 0:
                        return ""
                    else:
                        for k in range(i, j):
                            if word[j-1][k] in vowels:
                                return word[j-1][k]
                else:
                    if i < len(word[j]) - 1:
                        if word[j][i+1] in vowels:
                            return word[j][i]
                    if i == len(word[j]) - 1:
                        if j == len(word) - 1:
                            return ""
                        else:
                            for k in range(i, j+1):
                                if word[j+1][k] in vowels:
                                    return word[j+1][k]
                        
    return ""


# def get_closest_vowel(word):
#     vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
#     word = word.split()
#     for j in range(len(word)-1, 0, -1):
#         for i in range(len(word[j])-1, 0, -1):
#             if word[j][i] == " ":
#                 continue
#             if word[j][i] in vowels:
#                 if i == 0:
#                     if j == 0:
#                         return ""
#                     else:
#                         for k in