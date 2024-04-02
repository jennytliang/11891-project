def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    
	Include these tokens in the code: m x _ ch _ cnt , ans =
	Do not include these tokens in the code: if type ( words ) != list
	"""
    def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    
	Include these tokens in the code: m x _ ch _ cnt , ans =
	Do not include these tokens in the code: if type ( words ) != list
	"""

    max_d = None

    for each_str in words:
        tmp_d = {}
        for each_char in each_str:
            tmp_d[each_char] = 1

        all_keys = tmp_d.keys()

        if max_d is not None:
            if len(all_keys) > len(max_d.keys()):
                max_d = tmp_d
            elif len(all_keys) == len(max_d.keys()):
                if sorted(all_keys)[0] < sorted(max_d.keys())[0]:
                    max_d = tmp_d

        else:
            max_d = tmp_d
    return max_d


    """write test cases"""

    # test_max = find_max(find_max(["name", "of", "string"]))
    # test_max = find_max(find_max(["name", "enam", "game"]))
    # test_max = find_max(find_max(["aaaaaaa", "bb" ,"cc"]))


# print(find_max(test_max))



# max = 0
# ans = ""
# for each_str in words:
#     print(each_str)
#     tmp_d = {}
#     print(tmp_d)
