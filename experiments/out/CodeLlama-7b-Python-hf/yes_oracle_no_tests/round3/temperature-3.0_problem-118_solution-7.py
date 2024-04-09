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
	Do not include these tokens in the code: pass get _
	"""
    # Rules:
    # 1) Vowels in the beginning and ending doesn't count.
    # 2) Return empty string if you didn't find any vowel met the above condition.
    # 3) You may assume that the given string contains English letter only.
    # 4) You may not use regular expressions

    # first, check if the word has vowels in it
    if ("a" in word) or ("e" in word) or ("i" in word) or ("o" in word) or ("u" in word): 
        # if it does, find the index of the last vowel
        vowel_index = len(word) - 1
        while vowel_index >= 0:
            if word[vowel_index] in "aeiou":
                break
            else:
                vowel_index -= 1
        # if the last vowel is the first or last letter, the word doesn't have any vowels in it
        if vowel_index == 0 or vowel_index == len(word) - 1:
            return ""
        else:
            # find the index of the first vowel to the right of the last vowel
            right_vowel_index = vowel_index + 1
            while right_vowel_index < len(word):
                if word[right_vowel_index] in "aeiou":
                    break
                else:
                    right_vowel_index += 1
            # if there is no vowel to the right of the last vowel, return empty string
            if right_vowel_index == len(word):
                return ""
            else:
                # if there is a vowel to the right of the last vowel, return the vowel
                return word[right_vowel_index]
    else:
        # if the word has no vowels, return empty string
        return ""

def main():
    print(get_closest_vowel("yogurt")) # "u"
    print(get_closest_vowel("FULL")) # "U"
    print(get_clos