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
    """
    if len(dict) == 0:
        return False

    case = None
    for k, v in dict.items():
        if k.isupper():
            if not case:
                case = 'upper'
            if case == 'lower':
                return False
        elif k.islower():
            if not case:
                case = 'lower'
            if case == 'upper':
                return False

    return True


def test_function(test_case):
    test_input, test_expected = test_case
    test_actual = check_dict_case(test_input)

    if test_actual == test_expected:
        test_text = "Pass"
    else:
        test_text = "Fail"

    print("{0}: {1}".format(test_text, test_input))
