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
    
	Include these tokens in the code:  def is _ v owel ( ch
	Do not include these tokens in the code: ow els =
	"""

    def is_vowel(char):
        return char in 'AEIOUaeiou'

    # TODO: Write your solution here
    # print(word)
    # print(word[::-1])
    # print(word[::-1].index('a'))
    # print(word[::-1].index('a') / 2)
    # print(word[::-1].index('a') % 2)
    # print(word[::-1].index('a') // 2)
    # print(word[::-1].index('a') % 2)

    # if len(word) == 0:
    #     return ''
    # if len(word) == 1:
    #     return ''
    # if len(word) == 2:
    #     return ''
    # if len(word) == 3:
    #     return ''
    # if len(word) == 4:
    #     return ''

    # if len(word) % 2 == 0:
    #     if is_vowel(word[len(word) // 2]):
    #         return word[len(word) // 2]
    #     else:
    #         return ''
    # else:
    #     if is_vowel(word[len(word) // 2]):
    #         return word[len(word) // 2]
    #     elif is_vowel(word[(len(word) // 2) - 1]):
    #         return word[(len(word) // 2) - 1]
    #     elif is_vowel(word[(len(word) // 2) + 1]):
    #         return word[(len(word) // 2) + 1]
    #     else:
    #         return ''

    # for i in range(len(word) // 2, len(word)):
    #     if is_vowel(word[i]):
    #         return word[i]
    # for i in range(len(word) // 2 - 1