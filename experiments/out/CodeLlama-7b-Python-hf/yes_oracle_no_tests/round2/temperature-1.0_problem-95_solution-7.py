def check_dict_case(dict):
    """
    Given a dictionary, return True if all keys are strings in lower 
    case or all keys are strings in upper case, else return False.
    The function should return False is the given dictionary is empty.
    Examples:
    check_dict_case({"a":"apple", "b":"banana"}) should return True.
    check_dict_case({"a":"apple", "A":"banana", "B":"banana"}) should return False.
    check_dict_case({"a":"apple", 8:"banana", "a":"apple"}) should return False.
    check_dict_case({"Name":"John", "Age":"36", "City":"Houston"}) should return False.
    check_dict_case({"STATE":"NC", "ZIP":"12345" }) should return True.
    
	Include these tokens in the code: keys = list (
	Do not include these tokens in the code: lower _
	"""

    keys = list(dict.keys())

    # check if all keys have the same length
    flag = len(set(len(key) for key in keys))

    if len(keys) == 0 or flag == False:
        return False

    if sum({key.isupper() for key in keys}) == len(keys):
        return True
    elif sum({key.islower() for key in keys}) == len(keys):
        return True
    else:
        return False


def main():

    print("Example 1. check_dict_case({'a': 'apple', 'b': 'banana', }) should return True.")
    print("Answer: {}".format(check_dict_case({'a':'apple', 'b':'banana'}) ))

    print("Example 2.  check_dict_case({'a': 'apple', 'A': 'banana'}) should return False.")
    print("Answer: {}".format(check_dict_case({'a':'apple', 'A':'banana'})))

    print("Example 3.  check_dict_case({'a': 'apple', 8: 'banana', 'a': 'apple'}) should return False.")
    print("Answer: {}".format(check_dict_case({'a':'apple', 8:'banana', 'a':'apple'})))

    print("Example 4.  check_dict_case({'Name': 'John', 'Age': '36', 'City':'Houston'}) should return False.")
    print("Answer: {}".format(check_dict_case({'Name': 'John', 'Age':'36', 'City':'Houston'})))

    print("Example 5.  check_dict_case({'STATE': 'NC', 'ZIP': '12345'}) should return True.")
    print("Answer: {}".format(check_dict_case({'STATE':'NC', 'ZIP':'12345'})))

    print("Example 6.  check_dict_case({'STATE': 'NC', 'ZipCode': '12345'