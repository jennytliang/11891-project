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
    
	Do not include these tokens in the code: # Your code here
	"""
    all_keys = dict.keys()
    all_keys = [str(x) for x in all_keys]
    all_keys = [x.lower() for x in all_keys]
    all_keys = set(all_keys)
    all_keys = list(all_keys)
    if len(all_keys) == 0:
        return False
    elif all(x.isupper() for x in all_keys) or all(x.islower() for x in all_keys):
        return True
    else:
        return False
    



















































































































































































































































































































































































import numpy as np

def is_floats(x) -> bool:
    # check if it is float; List[float]; Tuple[float]
    if isinstance(x, float):
        return True
    if isinstance(x, (list, tuple)):
        return all(isinstance(i, float) for i in x)
    if isinstance(x, np.ndarray):
        return x.dtype == np.float64 or x.dtype == np.float32
    return False


def assertion(out, exp, atol):
    exact_match = out == exp

    if atol == 0 and is_floats(exp):
        atol = 1e-6
    if not exact_match and atol != 0:
        np.testing.assert_allclose(out, exp, atol=atol)
    else:
        assert exact_match


def check(candidate):
    inputs = [[{'p': 'pineapple', 'b': 'banana'}], [{'p': 'pineapple', 'A': 'banana', 'B': 'banana'}], [{'p': 'pineapple', '5': 'banana', 'a': 'apple'}], [{'Name': 'John', 'Age': '36', 'City': 'Houston'}], [{'STATE': 'NC', 'ZIP': '12345'}], [{'fruit': 'Orange', 'taste': 'Sweet'}], [{}], [{'FIRST_NAME': 'John', 'LAST_NAME': 'DOE', 'AGE': 35, 'CITY': 'NEW YORK', 'INCOME': '$50,000'}], [{'first_name': 'John', 'last_name': 'Doe', 'age': 35, 'city': 'New York', 'income': '$50,000'}], [{'firstName': 'John', 'LASTNAME': 'DOE', 'Age': 35, 'cItY': 'new york', 'Income': '$50,000'}], [{'first_name': 'John', 'Last_Name': 'Doe', 'Age': 35, 'city': 'New York', 'Income': '$50,000', 'FIRST_NAME': 'Jane'}], [{'1': 'apple', '2': 'banana', '3': 'cherry'}], [{'orange': 'fruit'}], [{'8': 'banana'}], [{'yellow': 'color'}], [{'2019': 'year'}], [{'PI': 3.14159}], [{'firstName': 'John', 'LASTNAME': 'DOE', 'Age': 35, 'Income': '$50,000'}], [{'first_name': 'John', 'Last_Name': 'Doe', 'city': 'New York', 'FIRST_NAME': 'cherry'}], [{'first_name': 'John', 'Age': 35, 'city': 'New York', 'Income': '$50,000', 'FIRST_NAME': 'Jane'}], [{'2019': 'yeyar'}], [{'1': 'apple', '2': 'banana', '3': 'cherry', 'Income': 'chINCEOMEerry'}], [{'FIRST_NAME': 'John', 'LAST_NAME': 'DOE', 'AGE': 35, 'CITY': 'NK', 'INCOME': '$50,000'}], [{'first_name': 'John', 'Last_Name': 'Dooe', 'Age': 35, 'city': 'New York', 'Income': '$50,000', 'FIRST_NAME': 'Jane', '1': 36, 'Incyellowome': 'INCOMEJohn'}], [{'firstName': 'John', 'LASTNAME': 'DOE', 'Age': 'D', 'cItY': 'new york', 'Income': '$50,000'}], [{'first_name': 'John', 'Last_Name': 'Dooe', 'Age': 35, 'city': 'New York', 'Income': '$50,000', 'FIRST_NAME': 'Jane', 'Incyellowome': 'INCOMEJohn'}], [{'FIRST_NAME': 'John', 'LAST_NAME': 'DOE', 'AGE': 35, 'CITY': 'NEW YORK', 'INCOME': '$50,000', 'COME': '$50,0000'}], [{'first_name': 'John', 'Age': 35, 'city': 'New York', 'Income': '$50,000', 'FIRST_NAME': 'Jane', '1': 36, 'Incyellowome': 'INCOMEJohn'}], [{'1': 'apple', '2': 'banana', '3': 'cherry', 'Income': 'New York'}], [{'yellow': 'color', 'yell': 'clor'}], [{'firstName': 'John', 'LASTNAME': 'DOE', 'Age': 35, 'cItY': 'new yorok', 'Income': '$50,000', 'cItIY': 36}], [{'firstName': 'John', 'LASTNAME': 'DOE', 'Age': 'D', 'cItY': 'new yorAgek', 'Income': '$50,000'}], [{'FIRST_NAME': 'John', 'LAST_NAME': 'DOE', 'AGE': 35, 'INCOME': '$50,000'}], [{'2': 'banana', '3': 'cherry', 'Income': 'New York', '$50,000': 'chrerry', 'Inconme': 'bana'}], [{'first_name': 'John', 'last_name': 'Doe', 'age': 35, 'city': 'New York', 'income': '$50,000', 'ageage': 'Dooe'}], [{'FIRST_NAME': 'John', 'LAST_NAME': 'DOE', 'AGE': 35, 'CITY': 'NK', 'INCOME': '$50,000', '1': 35}], [{'firstName': 'John', 'LASTNAME': 'DOE', 'Age': 'D', 'cItY': 'new yorAgek', 'Income': '$50,000', 'IncIome': 'FIRST_NAME'}], [{'firstName': 'John', 'LASTNAME': 'DOE', 'Age': 'D', 'cItY': 'new yorAgek', 'Income': '$50,000', 'LASTNAE': 'new yorAgeIncIomek'}], [{'2': 'banana', '3': 'cherry', 'Income': 'New York'}], [{'first_name': 'John', 'Last_Name': 'Doe', 'Age': 35, 'city': 'new yorAgek', 'Income': '$50,000', 'FIRST_NAME': 'Jane'}], [{'firstName': 'John', 'LASTNAME': 'DOE', 'Age': 'D', 'cItY': 'new yorAgek', 'IncIome': 'FIRST_NAME'}], [{'first_name': 'John', 'last_name': 'Doe', 'age': 35, 'city': 'New York', 'income': '$50,000', 'ageage': 'Dooe', 'new yorok': '8'}], [{'firstName': 'John', 'LASTNAME': 'DDOE', 'Age': 'D', 'cItY': 'new yorAgek', 'Income': '$50,000', 'IncIome': 'FIRST_NAME', 'LASTENAME': 'Anew yorAgek'}], [{'first_name': 'John', 'last_name': 'Doe', 'age': 35, 'city': 'New YorNk', 'income': '$50,000'}], [{'first_name': 'John', 'Last_Name': 'Doe', 'city': 'New York', 'Income': '$50,000', 'FIRST_NAME': 'Jane'}], [{'first_name': 'John', 'Last_Name': 'Doe', 'city': 'New Yoincomerk', 'Income': '$50,000', 'FIRST_NAME': 'Jane'}], [{'FIRST_NAME': 'John', 'LAST_NAME': 'OE', 'AGE': 35, 'CITY': 'NEW YORK', 'COME': '$50,0000'}], [{'firstName': 'John', 'Age': 35, 'Income': '$50,000', 'Incomeyeyar': 'JoDooehn'}], [{'firstName': 'John', 'LASTNAME': 'DOE', 'Age': 35, 'Income': '$50,000', '8': '$0,000'}], [{'firstName': 'Johageage', 'Age': 35, 'cItY': 'new york', 'Income': '$50,000'}], [{'PI': 3.14159, 'IPI': 2.6443947966293897, 'Johageage': 2.9360614575298136, 'JohaJgeage': 3.14159}], [{'first_name': 'John', 'Last_Name': 'Dooe', 'Age': 35, 'city': 'New York', 'Income': '$50,000', 'FIRST_NAME': 'Jane', '1': 36, 'Incyellowome': 'INCOMEJohn', 'chINCEOMEerryAge': '$50,00'}], [{'orange': 'fruuit', 'or$50,00ange': 'fruui'}], [{'first_name': 'oJohn', 'Last_Name': 'Doe', 'city': 'New York'}], [{'firstName': 'John', 'LASTNAME': 'DOE', 'Age': 'IPI', 'cItY': 'new yorAgek', 'Income': '$50,000', 'IncIome': 'FIRST_NAME'}], [{'firstName': 'John', 'LASTNAME': 'DOE', 'Age': 'D', 'Income': '$50,000'}], [{'firstName': 'John', 'Age': 'bana', 'cItY': 'new yorAgek', 'Income': '$50,000', 'LASTNAE': 'new yorAgeIncIomek'}], [{'first_name': 'John', 'Age': 35, 'Income': '$50,000', 'FIRST_NAME': 'Jane'}], [{'PI': 1.7300435058060522}], [{'first_name': 'John', 'Last_Name': 'Dooe', 'Age': 35, 'city': 'New York', 'Income': '$50,000', 'FIRST_NAME': 'Jane', '1': 36, 'Incyellowome': 'INCOMEJohn', 'chINCEOMEerryAge': '$50,00', 'chge': 'New YorkLAST_NAME', 'New York': 'new york'}], [{'firstName': 'John', 'LASTNAME': 'DDOE', 'Age': 'D', 'Income': '$50,000', 'IncIome': 'FIRST_NAME'}], [{'firstName': 'John', 'LASTNAME': 'DOlast_nameE', 'Age': 35, 'cItY': 'new yorok', 'Income': '$50,000', 'cItIY': 36}], [{'first_name': 'John', 'Last_Name': 'Doe', 'city': 'New York'}], [{'2019': 'firstName', 'YorNk': 'firstNam$50,0000e', 'NEW YORK': 'fDOlast_nameEirstName'}], [{'orange': 'JoDooehn', 'Dooe': 'JoDooehhn'}], [{'FIRST_NAME': 'John', 'LAST_NAME': 'OE', 'AGE': 35, 'CITY': 'NEW YORK', 'COME': '$50,0000', 'YORK': '$50,00000'}], [{'firstName': 'John', 'LASTNAME': 'DOE', 'Age': 'D', 'cItY': 'new yorAgekcolor', 'Income': '$50,000'}], [{'first_name': 'John', 'last_name': 'Doe', 'age': 35, 'city': 'oNew YorNk', 'income': '$50,000', 'Newage': '2,000'}], [{'first_name': 'John', 'last_name': 'Doe', 'age': 35, 'income': '$50,000', 'ageage': 'Dooe', 'new yorok': '8'}], [{'firstName': 'John', 'LASTNAME': 'DOE', 'Age': 'D', 'Income': 'YORK'}], [{'yellow': 'orange'}], [{'FIRST_NAME': 'John', 'LAST_NAME': 'OE', 'AGE': 35, 'CITY': 'NEW YORK', 'COME': '$50,0000', 'John': 'year'}], [{'orange': 'JoDooehn', 'Dooe': 'JoDooehhn', 'LAST_NAME': 'NK'}], [{'PI': 1.7300435058060522, 'New YorkLAST_NAMEPI': 2.6189164796316335, 'cItIY': 2.6443947966293897}], [{'yellow': 'oDDOErange'}], [{'firstName': 'John', 'LASTNAME': 'DOE', 'Age': 35, 'cItY': 'new yorrk', 'Income': '$50,000', 'CITY': 'DOfDOlast_nameEirstNameE'}], [{'first_name': 'John', 'Last_Name': 'Doe', 'city': 'new yorAgek', 'Income': '$50,000', 'FIRST_NAME': 'Jane'}], [{'first_name': 'John', 'Age': 35, 'city': 'New York', 'Income': '$50,000', 'FIRST_NAME': 'Jane', '1': 36, 'Incyellowome': 'INCOMEJohn', 'orange': 'INCOMEJohn'}], [{'first_name': 'John', 'Last_Name': 'Doe', 'Age': 35, 'Income': '$50,000', 'FIRST_NAME': 'Jane', '': 35, 'fruuit': 34}], [{'orange': 'ruuit', 'or$50,00ange': 'fruui'}], [{'firstName': 'John', 'LASTNAME': 'DOE', 'Age': 'D', 'cItY': 'new yorAgekcolor', 'Income': '$50,000', 'firstN': 'JohaJgeage', 'cItAGEY': 'JJoDooehhnohaJgeage'}], [{'first_name': 'John', 'Last_Name': 'Dooe', 'Age': 35, 'city': 'New York', 'Income': '$50,000', 'FIRST_NAME': 'Anew', '1': 36, 'Incyellowome': 'INCOMEJohn', 'chINCEOMEerryAge': '$50,00'}], [{'PI': 3.14159, 'IPI': 2.6443947966293897, 'Johageage': 2.9360614575298136, 'JohaJgeage': 3.14159, 'PPI': 2.9360614575298136}], [{'firstName': 'John', 'LASTNAME': 'DOE', 'Age': 'IP', 'Income': '$50,000', 'IncIome': 'FIRST_NAME'}], [{'first_name': 'John', 'Last_Name': 'Dooe', 'Age': 35, 'city': 'New York', 'Income': '$50,000', 'FIRST_NAME': 'Anew', '1': 36, 'Incyellowome': 'INCOMEJohn', 'chINCEOMEerryAge': '$50,00', 'Last_Namme': 'fruit'}], [{'first_name': 'John', 'last_name': 'Doe', 'age': 36, 'city': 'New YorNk', 'income': 'bana'}], [{'PI': 1.7300435058060522, 'New YorkLAST_NAMEPI': 2.6189164796316335, 'cItIY': 2.6443947966293897, 'New YorkLASTcity_NAMEPI': 2.3210819853008124}], [{'first_name': 'JIncomeyeyarohn', 'Last_Name': 'Dooe', 'Age': 35, 'city': 'New York', 'Income': '$50,000', 'FIRST_NAME': 'Jane', '1': 36, 'Incyellowome': 'INCOMEJohn'}], [{'FIRST_NAME': 'John', 'AGE': 35, 'CITY': 'NEW YORK', 'COME': '$50,0000', 'John': 'year'}], [{'FIRST_NAME': 'John', 'LAST_NAME': 'DOE', 'AGE': 35, 'INCOME': '$50,000', 'Age': 35}], [{'PI': 1.7300435058060522, 'new yorrk': 2.2762868739904514}], [{'first_name': 'John', 'Age': 35, 'FIRST_NAME': 'Jane'}], [{'first_name': 'John', 'last_name': 'Doe', 'age': 36, 'income': 'bana'}], [{'Age': 35}], [{'first_name': 'John', 'Last_Name': 'Doe', 'city': 'new yorAgek', 'Income': '$50,000', 'FIRST_NAME': 'Jane', '_FIRST_NAME': 'JNew YorNke', 'new yorAgeIncIomekIncome': '1'}], [{'PI': 1.7300435058060522, 'New YorkLAST_NAMEPI': 2.6189164796316335, 'cItIY': 2.6443947966293897, 'I': 2.7107068449059466}], [{'firstName': 'Joohn', 'LASTNAME': 'DOE', 'Age': 'IPI', 'cItY': '2', 'Income': '$50,000', 'IncIome': 'FIRST_NAME'}], [{'LASTNAME': 'DOE', 'Age': 'IPI', 'cItY': '2', 'Income': '$50,000', 'IncIome': 'FIRST_NAME'}], [{'orange': 'fruurit', 'or$50,00ange': 'fruui'}], [{'firstName': 'John', 'LASTNAME': 'DDOE', 'Age': 'D', 'cItY': 'new yorAgek', 'Income': '$50,000', 'IncIome': 'FIRST_NAME', 'LASTENAME': 'Anew yorAgek', 'IncYorkLASTcity_NAMEPIIome': 'Anenew yorAgeIncIomekw yorAgek', 'ageage': 'cItYnew yorAgek'}], [{'orange': 'fruurit', 'or$50,00ange': 'fruui', 'orYoincomerk$50,00ange': 'fruuritt'}], [{'first_name': 'John', 'Last_Name': 'Doe', 'city': 'NNew YorkLASTcity_NAMEPIew York', 'tfirst_name': 'JohJIncomeyeyarohnn'}], [{'PI': 1.9949170779000351}], [{'LASTNAME': 'DOE', 'Age': 'IPI', 'cItY': '2', 'Income': '$50,000', 'IncIome': 'FIRfirstNam$50,0000eST_NAME'}], [{'firstName': 'John', 'LASTNAME': '1DOE', 'Age': 'D', 'Income': 'YorkLASTcity_NAMEPI'}], [{'first_name': 'John', 'Last_Name': 'DYorNkoe', 'city': 'New York', 'FIRST_NAME': 'cherry'}], [{'PI': 1.7300435058060522, 'New YorkLAST_NAMEPI': 2.6189164796316335, 'cItIY': 2.6443947966293897, 'New YorkLAST_NALast_NammeMEPI': 0.8622214662877261}], [{'firstName': 'Joohn', 'LASTNAME': 'DOE', 'cItY': '2', 'IncIome': 'FIRST_NAME'}], [{'firstName': 'John', 'LASTNAME': 'clor', 'Age': 'D', 'Income': 'YORK'}], [{'2': 'banana', '3': 'cherry', 'Income': 'NewYork'}], [{'first_name': 'John', 'Last_Name': 'Dooe', 'Age': 35, 'city': 'New York', 'FIRST_NAME': 'Jane', '1': 36, 'Incyellowome': 'INCOMEJohn', 'chINCEOMEerryAge': '$50,00'}], [{'PI': 1.7300435058060522, 'New YorkLAST_NAMEPI': 2.6189164796316335, 'cItIY': 2.6443947966293897, 'New YorkLASTcity_NAMEPI': 2.3210819853008124, 'NNew YorkLASTcity_NAMEPIew York': 2.2786871475765835}], [{'first_name': 'John', 'last_name': 'Doe', 'income': '$50,000', 'ageage': 'Dooe', 'new yorok': '8'}], [{'2': 'banana', '3': 'cherry', 'Income': 'New Yk', '$50,000': 'chrerry', 'Inconme': 'bana'}], [{'firstName': 'John', 'LASTNAME': 'DOE', 'Age': 36, 'Income': '$50,000', '8': '$0,000'}], [{'PI': 1.7300435058060522, 'New YorkLAST_NAMEPI': 2.6189164796316335, 'cItIY': 2.6443947966293897, 'I': 2.9360614575298136, '8PI': 2.2268929884240265, 'JohJIncomeyeyarohnn': 1.9949170779000351}], [{'LASTNAME': 'DOE', 'Age': 'D', 'cItY': 'new yorAgek', 'Income': '$50,000', 'IncIome': 'FIRST_NAME'}], [{'firstName': 'Jooohn', 'LASTNAME': 'DOE', 'cItY': '2', 'IncIome': 'FIRST_NAME', 'Anew yorAgek': 'FIRSTNAME'}], [{'first_name': 'John', 'Last_Name': 'Do', 'Age': 35, 'city': 'New York', 'Income': '$50,000', 'FIRST_NAME': 'Anew', '1': 36, 'Incyellowome': 'INCOMEJohn', 'chINCEOMEerryAge': '$50,00', 'Last_Namme': 'fruit'}], [{'firstName': 'John', 'LASTNAME': 'DOE', 'Age': 36, 'Income': '$50,000', '8': '$0,000', 'firslast_nametName': 'cherry'}], [{'1': 'apple', '2': 'banana', '3': 'cherry', 'Income': 'chINCEOMEerry', 'CITY3': 'cherr'}], [{'orange': 'oDDOErange', 'or$50,00ange': 'fruui'}], [{'2': 'banana', '3': 'cherry', '$50,000': 'chrerry', 'Inconme': 'bana'}], [{'1': 'apple', '2': 'orange', '3': 'cherry', 'Income': 'chINCEOMEerry'}], [{'1': 'apple', '2': 'orange', '3': 'cherry', 'Income': 'chINCEOMEOerry'}], [{'Dooe': 'fruuritt', 'LAST_NAAME': 'JNew YorNkeJoDooehn'}], [{'PI': 1.7300435058060522, 'cItIY': 2.6443947966293897, 'New YorkLAST_NALast_NammeMEPI': 0.8622214662877261}], [{'first_name': 'John', 'Age': 35, 'FIRST_NAME': 'Jane', 'AAge': 'Jcherrohn'}], [{'first_name': 'John', 'Last_Name': 'Doe', 'Age': 35, 'city': 'Newor$50,00ange York', 'Income': '$50,000', 'FIRST_NAME': 'Jane', 'Incoome': 'oJohn'}], [{'firstName': 'John', 'LASTNAME': 'DOE', 'Age': 'D', 'cItY': 'new yorAgek', 'Income': '$50,000', 'IncIomNNew YorkLASTcity_NAMEPIew Yorke': 'CITY3'}], [{'first_name': 'John', 'Last_Name': 'Doe', 'Age': 35, 'city': 'Newor$50,00ange York', 'Income': '$50,000', 'FIRST_NAME': 'Jane', 'Incoome': 'oJohn', '': 'oJoh'}], [{'first_name': 'John', 'Last_Name': 'DYorNkoe', 'FIRST_NAME': 'cherry'}], [{'PI': 1.7300435058060522, 'New YorkLAST_NAMEPI': 2.1459305021091426, 'cItIY': 2.6443947966293897, 'New YorkLASTcity_NAMEPI': 2.3210819853008124}], [{'LASTNAME': 'DOE', 'Age': 'D', 'Income': '$50,000', 'IncIome': 'FIRST_NAME'}], [{'firstName': 'John', 'LASTNAME': 'DOE', 'Age': 36, 'cItY': 'new yorrk', 'Income': '$50,000', 'CITY': 'DOfDOlast_nameEirstNameE'}], [{'first_name': 'John', 'Last_Name': 'Do', 'Age': 35, 'city': 'New York', 'Income': '$50,000', 'FIRST_NAME': 'Anew', '1': 36, 'Incyellowome': 'INCOMEJohn', 'chINCEOMEerryAge': '$50,00', 'Last_Namme': 'fruit', 'fDOlast_nameEirstName': 'NNewYork'}], [{'FIRST_NAME': 'John', 'LAST_NAME': 'OE', 'AGE': 35, 'COME': '$50,0000', 'YORK': 'Anenew', 'Jcherrohn': 'chINCEOMEerryAnenew'}], [{'firstName': 'John', 'LASTNAME': 'DDOE', 'Income': '$50,000', 'IncIome': 'FIRST_NAME'}], [{'Last_Name': 'Do', 'Age': 35, 'city': 'New York', 'Income': '$50,000', 'FIRST_NAME': 'Anew', '1': 36, 'Incyellowome': 'INCOMEJohn', 'chINCEOMEerryAge': '$50,00', 'Last_Namme': 'fruit', 'fDOlast_nameEirstName': 'NNewYork'}], [{'firstName': 'John', 'LASTNAME': 'DOE', 'Age': 'IPI', 'cItY': 'new yorAgek', 'Income': '$50,000', 'IncIome': 'FIRST_NAME', 'LAST_NAME': '$$50,000'}], [{'first_name': 'John', 'last_name': 'Doe', 'age': 35, 'city': 'New YorNk', 'income': '$50,000', 'New Yk': '$5fruuritt0,000'}], [{'LASTNAME': 'DOE', 'Age': 'D', 'cItY': 'nenew yorAgeIncIomekw yorAgek', 'Income': '$50,000', 'IncIome': 'FIRST_NAME'}], [{'FIRST_NAME': 'John', 'AGE': 35, 'INCOME': '$50,000'}], [{'firstName': 'John', 'LASTNAME': 'DOE', 'Age': 35, 'cItY': 'new yorrk', 'CITY': 'DOfDOlast_nameEirstNameE', 'CITTY': 35}], [{'first_name': 'John', 'last_name': 'yorAgeIncIomek', 'age': 35, 'city': 'New York', 'income': '$50,000', 'New Yk': 34}], [{'PI': 1.7300435058060522, 'new yorrk': 2.2762868739904514, 'new ryorrk': 1.7300435058060522, 'new ryorLast_Namerk': 2.6443947966293897}], [{'firstName': 'John', 'LASTNAME': 'DOE', 'Age': 'IPI', 'cItY': 'new yorAgek', 'Income': '$50,000', 'IncIome': 'FIRST_NAME', 'firsnew yorAgektName': 'new yogrAgek', 'ccItAGEYItY': 'new yogrAgekk'}], [{'LAST_NAME': 'DOE', 'AGE': 36, 'INCOME': '$50,000', 'Age': 35}], [{'first_name': 'John', 'Last_Name': 'Doe', 'Age': 35, 'city': 'New York', 'Income': '$50,000', 'FIRST_NAME': 'Jane', 'Incoome': 'kNew York'}], [{'first_name': 'John', 'Last_Name': 'Dooe', 'Age': 35, 'city': 'New York', 'Income': '$50,000', 'FIRST_NAME': 'Jane', '1': 36, 'Incyellowome': 'INCOMEJohn', 'IncIncYorkLASTcity_NAMEPIIomelowome': 'New YoJohageagek'}], [{'2019': '', '20new yorrk19': 'Newor$50,00ange'}], [{'2': 'banana', '3': 'cherry', 'Income': 'chINCEOMEerry'}], [{'first_name': 'John', 'last_name': 'Doe', 'age': 35, 'city': 'New York', 'income': '$50,000', 'ageage': 'Inconme'}], [{'first_name': 'John', 'Last_Name': 'DYorNkoe', 'city': 'New York', 'FIRST_NAME': 'cherry', 'Last_Namme': 'yeyar'}], [{'PI': 3.14159, 'IPI': 2.6443947966293897, 'Johageage': 2.9360614575298136, 'JohaJgeage': 3.14159, 'IIPI': 1.690316164828218}], [{'firstName': 'Joohn', 'LASTNAME': 'DOE', 'cItY': '2', 'Income': '$50,000', 'IncIome': 'FIRST_NAME'}], [{'firstName': 'John', 'Age': 36, 'Income': '$50,000', '8': '$0,000'}], [{'first_name': 'John', 'Last_Name': 'Dooe', 'Age': 35, 'city': 'New York', 'Income': '$50,000', 'FIRST_NAME': 'Jane', '1': 36, 'Incyellowome': 'INCOMEJohn', 'chINCEOMEerryAge': '$50,00', 'Newor$50,00ange': 'NNewYork'}], [{'first_name': 'John', 'Last_Name': 'Dooe', 'Age': 35, 'city': 'New York', 'Income': '$0,000', 'FIRST_NAME': 'Jane', '1': 37, 'Incyellowome': 'INCOMEJohn', 'IncIncYorkLASTcity_NAMEPIIomelowome': 'New YoJohageagek'}], [{'yellow': 'oraNewnge'}], [{'first_name': 'John', 'Last_Name': 'Dooe', 'Age': 35, 'city': 'New York', 'Income': '$0,000', 'FIRST_NAME': 'Jane', '1': 37, 'Incyellowome': 'INCOMEJohn', 'IncIncYorkLASTcity_NAMEPIIomelowome': 'New YoJohageagek', 'IncIncYorkLASJanelowome': 'New'}], [{'firstName': 'John', 'LASTNAME': 'DOE', 'Age': 'D', 'cItY': 'new york'}], [{'first_name': 'John', 'Last_Name': 'Doe', 'Age': 35, 'city': 'NewNEWor$50,00ange York', 'Income': '$50,000', 'FIRST_NAME': 'Jane', 'Incoome': 'oJohn', 'Agee': '$50,0oNew YorNk00'}], [{'firstName': 'hJohn', 'LASTNAME': 'DOE', 'Age': 35, 'Income': '$50,000', '8': '$0,000'}], [{'FIRST_NAME': 'John', 'LAST_NAME': 'DOE', 'AGE': 35, 'INCOME': '$50,000', 'IfDOlast_nameEirstNameNCOME': 35}], [{'LAST_NAME': 'oJoh', 'AGE': 35, 'CITY': 'NK', 'INCOME': '$50,000', '1': 35}], [{'or$50,00ange': 'fruui'}], [{'FIRST_NAME': 'John', 'LAST_NAME': 'DOE', 'AGE': 35, 'CITY': 'NEW YORK', 'COME': '$50,0000'}], [{'firstName': 'Jooohn', 'LASTNAME': 'YorNke', 'cItY': '2', 'IncIome': 'FIRST_NAME', 'Anew yorAgek': 'FIRSTNAME'}], [{'first_name': 'John', 'Age': 35, 'city': 'New York', 'Income': '$50,000', 'FIRST_NAME': 'Jane', '1': 36, 'Incyellowome': 'INCOMEJohn', 'Anenew': 'INCOMEJJohn'}], [{'first_name': 'John', 'Age': 35, 'city': 'New York', 'Income': '$50,000', '1': 36, 'Incyellowome': 'INCOMEJohn'}], [{'first_name': 'John', 'Age': 35, 'city': 'New York', 'Income': '$50,000', 'FIRST_NAME': 'Jane', '1': 36, 'Incyellowome': 'INCOMEJohn', 'chINCEOMEerryAge': '$50,00', 'firsnew yorAgektName': 'new yorAgeIncIomekIncome'}], [{'first_name': 'John', 'Last_Name': 'Dooe', 'Age': 35, 'Income': '$50,000', 'FIRST_NAME': 'Jane', 'Incyellowome': 'INCOMEJohn'}], [{'PI': 1.7300435058060522, 'new ryorrk': 1.7300435058060522, 'new ryorLast_Namerk': 2.6443947966293897}], [{'FIRST_NAME': 'John', 'LAST_NAME': 'DOE', 'AGE': 35, 'INCOME': '$50,000', 'new yorAgek': 'DOYorkLAST_NAMEPI'}], [{'yelelow': 'CyellOME', 'yelew': 'New YorkLAST_NAMEPI'}], [{'LASTNAME': 'DOE', 'Age': 'IPI', 'cItY': '2', 'IncIome': 'FIRfirstNam$50,0000eST_NAME', 'InceIome': 'Last_Namme'}], [{'first_name': 'John', 'Last_Name': 'Doe', 'Age': 35, 'city': 'new yorAgek', 'Income': '$50,,000', 'FIRST_NAME': 'Jane'}], [{'Dooe': 'fruuritt', 'LAST_NAAME': 'JNew YorNkeJoDooehn', 'Age': 'ffruuritt'}], [{'firstName': 'Jooohn', 'LASTNAME': 'YorNke', 'cItY': '2', 'IncIome': 'yorAgeIncIomek', 'Anew yorAgek': 'FIRSTNAME'}], [{'first_name': 'John', 'Last_Name': 'Doe', 'city': 'new yorAgek', 'Income': '$50,000', '_FIRST_NAME': 'JNew YorNke', 'new yorAgeIncIomekIncome': '1'}], [{'PI': 1.7300435058060522, 'new yorrk': 2.2762868739904514, 'new yrk': 1.6108425454874835}], [{'first_name': 'John', 'Last_Name': 'Doe', 'Age': 35, 'city': 'new yorAgek', 'Income': '$50,000', 'FIRST_NAME': 'Jane', 'DDOEIncome': '$50,00'}], [{'yelelow': 'CyellOME', 'yelew': 'NewT_NAMEPI'}], [{'first_name': 'John', 'Age': 35, 'city': 'New York', 'Income': '$50,000', 'FIRST_NAME': 'Jane', '1': 36, 'Incyellowome': 'INCOMEJohn', 'chINCEOMEerryAge': '$50,00', 'firsnew yorAgektName': 'new yorAgeIncIomekIncome', 'citty': 'Jon'}], [{'first_name': 'John', 'Age': 35, 'city': 'NewY York', 'Income': '$50,000', 'FIRST_NAME': 'Jane', 'Incom2019e': 'Joh2,000n'}], [{'3': 'cherry', '$50,000': 'chrerry'}], [{'first_name': 'John', 'Last_Name': 'Dooe', 'Age': 35, 'Income': '$50,000', 'FIRST_NAME': 'Jane', 'Incyellowome': 'YorNk00', 'CITY': 'Doe', 'yogrAgekk': 'Do$$50,000e'}], [{'firstName': 'John', 'LASTNAME': 'DOE', 'Age': 36, 'cItY': 'new yorok', 'Income': '$50,000', 'cItIY': 36}], [{'PI': 1.7300435058060522, 'New YorkLAST_NAMEPI': 2.6189164796316335, 'cItIY': 2.6443947966293897, 'New YorkLASTcity_NAMEPI': 2.3210819853008124, 'New YorkLAST_NPAMEPI': 1.3462361524091344}], [{'first_name': 'John', 'Last_Name': 'Dooe', 'Age': 35, 'Income': '$50,000', 'FIRST_NAME': 'Jane', 'Incyellowome': 'INCOMEJohn', 'first_namme': '$50,0last_name00'}], [{'PI': 1.7300435058060522, 'cItIY': 2.6443947966293897, 'New YorkLAST_NALast_NammeMEPI': 0.17904925194593924}], [{'FIRST_NAME': '2019n', 'LAST_NAME': 'OE', 'AGE': 35, 'CITY': 'NEW YORK', 'COME': '$50,0000'}], [{'last_name': 'Doe', 'income': '$50,000'}], [{'LASTNAME': 'DOE', 'Age': 'IPI', 'cItY': 'new yorAgek', 'Income': '$50,000', 'IncIome': 'FIRST_NAME', 'firsnew yorAgektName': 'new yogrAgek', 'ccItAGEYItY': 'new yogrAgekk'}], [{'last_name': 'Doe', 'age': 35, 'city': 'New York', 'ageage': 'Inconme'}], [{'Age': 35, 'cItY': 'new york', 'Income': '$50,000'}], [{'first_name': 'John', 'Last_Name': 'Doe', 'city': 'new yrk'}], [{'LASTNAME': 'DOE', 'Age': 'IPI', 'cItY': '2', 'Income': '$500,000', 'IncIome': 'FIRST_NAME'}], [{'LAST_NAME': 'oJoh', 'AGE': 35, 'CITY': 'NK', '1': 35, 'AE': 'new'}], [{'first_name': 'John', 'Age': 35, 'city': 'new yorAgek', 'Income': '$50,,000', 'FIRST_NAME': 'Jane'}], [{'firstName': 'Jooohn', 'LASTNAME': 'YorNke', 'cItY': '2', 'IncIome': 'yorAgeIncIomek', 'Anew yorAgek': 'FIRSTNAME', 'year': 'first_name'}], [{'LASTNAME': 'DOE', 'Age': 'IPI', 'cItY': '2', 'Income': '$50,000', 'IncIome': 'FIRST_NAME', 'Do': 'EDOE'}], [{'firstName': 'Joohn', 'LASTNAME': 'DOE', 'cItY': '2', 'IncIome': 'FIRST_NAME', 'Jon': 'Joohnn'}], [{'firstName': 'Joohn', 'LASTNAME': 'DOE', 'Income': '$50,000', 'IncIome': 'FIRST_NAME', 'LANewY YorkSTNAME': 'OE'}], [{'firstName': 'John', 'LASTNAME': 'DDOE', 'Income': '$50,0000', 'IncIome': 'FIRST_NAME'}], [{'firstName': 'John', 'LASTNAME': 'DOE', 'Age': 'D', 'Income': 'firsnew', 'firstsName': 'YoincomerkD'}], [{'firstName': 'John', 'LASTNAME': 'DOE', 'Age': 35, 'cItY': 'new yorrk', 'Income': '$50,000', 'CITY': 'DOfDOlast_nameEirstNameE', 'NEW': '1'}], [{'LASTNAME': 'DOE', 'Age': 'D', 'cItY': 'new yorAgek', 'Income': '$50,000', 'LASTNAE': 'new yorAgeIncIomek'}], [{'firstName': 'John', 'LASTNAME': 'DOE', 'Age': 'D', 'cItY': 'new yorAgekcolor', 'yorok': 'Jooohn'}], [{'LASTNAME': 'DOE', 'Age': 'IPI', 'cItY': '2', 'Income': '$500,000', 'IncIome': 'FIRST_NAME', 'Incomeyeyar': 'AAge'}], [{'firstName': 'John', 'Age': 'bana', 'cItY': 'new yorAgek', 'Income': '$00', 'LASTNAE': 'new yorAgeIncIomek', 'Inc': 'JNew'}], [{'firstName': 'John', 'LASTNAME': 'DOE', 'Age': 35, 'Income': '$50,000', 'FIRST_NAME': 36}], [{'FIRST_NAME': 'John', 'COME': '$50,0000', 'John': 'year', 'yorrk19': 'yellow', 'income': 'yelelow'}], [{'PI': 1.7300435058060522, 'New YorkLAST_NAMEPI': 2.6189164796316335, 'cItIY': 2.6443947966293897, 'I': 2.7107068449059466, 'CyellOME': 1.6243371737850312}], [{'Dooe': 'JoDooehhn'}], [{'firstName': 'John', 'LASTNAME': 'DDOE', 'Age': 'D', 'cItY': 'new yorAgek', 'Income': '$50,000', 'IncIome': 'FIRST_NAME', 'LASTENAME': 'Anew yorAgek', 'cItcY': 'DD'}], [{'LASTNAME': 'DOE', 'Age': 'D', 'cItY': 'nenew yorAgeIncIomekw yorAgek', 'Income': '$50,000NNewYork', 'IncIome': 'FIRST_NAME', 'eAge': 'Yoincomerk'}], [{'first_name': 'oJohn', 'Last_Name': 'DLAST_NAJohnMEe', 'city': 'New York'}], [{'LAST_NAME': 'oJoh', 'AGE': 35, 'CITY': 'NK', '1': 34, 'AE': 'new'}], [{'LASTNAME': 'DOE', 'Age': 'IPI', 'cItY': '2', 'Income': '$50eAge,000', 'IncIome': 'Anenew yorAgeIncIomekw yorAgek', 'Do': 'EDOE'}], [{'PI': 1.8117899160754405}], [{'2019': 'firstName', 'YorNk': 'firstNe', 'NEW YORK': 'fDOlast_nameEirstName'}], [{'PI': 1.7300435058060522, 'New YorkLAST_NAMEPI': 2.6189164796316335, 'I': 2.7107068449059466, 'CyellOME': 1.6243371737850312}], [{'PI': 2.7107068449059466}], [{'first_name': 'John', 'Last_Name': 'Do', 'Age': 35, 'city': 'New York', 'Income': '$50,000', 'FIRST_NAME': 'Anew', '1': 36, 'Incyellowome': 'INCOMEJohn', 'chINCEOMEerryAge': '$50,00', 'Last_Namme': 'fruit', 'citiy': '8PI'}], [{'FIRST_NAME': 'John', 'LAST_NAME': 'OE', 'AGE': 35, 'CITY': 'NEW YORK', 'COME': '$50,0000', 'YORK': '$50,00000', 'FIRFIRSTNAMEAME': '$ryorLast_Namerk50,00000'}], [{'LASTNAME': 'DOcitiyE', 'Age': 'D', 'cItY': 'new yorAgek', 'Income': '$50,000'}], [{'first_name': 'John', 'Age': 35, 'city': 'New York', 'FIRST_NAME': 'Jane', 'Incyellowome': 'INCOMEJohn'}], [{'firstName': 'John', 'LASTNAME': 'DODE', 'Age': 'D', 'cItY': 'new york'}], [{'first_name': 'John', 'Last_Name': 'Dooe', 'Age': 35, 'Income': '$50,000', 'FIRST_NAME': 'Jane', 'CITY': 'Doe', 'yogrAgekk': 'Do$$50,000e', 'Last_eName': 'JanLast_Namee', 'cItIY': 'JafirstsNamee'}], [{'PI': 2.2762868739904514}], [{'PI': 3.14159, 'IPI': 2.6443947966293897, 'Johageage': 1.6108425454874835, 'JohaJgeage': 3.14159, 'PPI': 2.9360614575298136}], [{'firstName': 'John', 'Age': 'D', 'Income': 'KYORK'}], [{'firstName': 'John', 'LASTNAME': 'DOE', 'cItY': 'new yorrk', 'Income': '$50,000', 'CITY': 'DOfDOlasNew Yoincomerkt_nameEirstNameE'}], [{'first_name': 'IncIomNNew', 'Last_Name': 'DYorNkoe', 'city': 'New York', 'FIRST_NAME': 'OE'}], [{'firstName': 'hJoohhn', 'LASTNAME': 'DOE', 'Age': 'IPI', 'cItY': '2', 'Income': '$50,000', 'IncIome': 'FIRST_NAME', 'IncIomme': 'DOfDOlasNew Yoincomerkt_nameEirstNameE'}], [{'firstName': 'JoDo$$50,000ehageage', 'Age': 35, 'cItY': 'new york', 'Income': '$50,000'}], [{'first_name': 'John', 'Last_Name': 'Doe', 'city': 'New York', 'Income': '$hJoohhn50,000', 'FIRST_NAME': 'Jane'}], [{'3': 'cherrfirstNy', '$50,000': 'chrerry'}], [{'firstName': 'Johhn', 'LASTNAME': 'DOE', 'Age': 'D'}], [{'firstName': 'John', 'LASTNAME': 'DOE', 'Age': 'D', 'Income': '$50,000', 'IncIomNNew YorkLASTcity_NAMEPIew Yorke': 'CITY3', 'fruuit': '2,000', 'hJoohhn': 'Johhn'}], [{'firstName': 'hJon', 'LASTNAME': 'DOE', 'Age': 35, 'Income': '$50,000', '8': '$0,000', 'IP': 36}], [{'firstName': 'John', 'Age': 'IPI', 'cItY': '$50,,000', 'Income': '$50,000', 'IncIome': 'FIRST_NAME', 'firsnew yorAgektName': 'new yogrAgek', 'ccItAGEYItY': 'new yogrAgekk'}], [{'firstName': 'Johhn', 'Age': 'D'}], [{'2': 'banana', '3': 'first_name', '2$0,000': 'chery'}], [{'LASTNAME': 'DOE', 'Age': 36, 'Income': '$50,000', '8': '$0,000', 'firslast_nametName': 'cherry'}], [{'firstName': 'John', 'LASTNAME': 'DOlast_nameE', 'Age': 35, 'cItY': 'new yorok', 'Income': '$50,000', 'cItIY': 37}], [{'LASTNAME': 'DOE', 'Age': 'D', 'Income': '$50,000', 'IncIome': 'FIRST_NAME', 'Joohn': 'DcItYnewOE'}], [{'LASTNAME': 'JNew YorNkeJoDooehn', 'Age': 'IPI', 'cItY': '2', 'Income': '$500,000', 'IncIome': 'FIRST_NAME', 'Incomeyeyar': 'AAge'}], [{'LASTNAME': 'DOE', 'Age': 'I', 'cItY': '2', 'InceIome': 'Last_Namme'}], [{'first_name': 'oJohn', 'Last_Name': 'DLAST_NAJohnMEe'}], [{'first_name': 'IncIomNNew', 'city': 'New York', 'FIRST_NAME': 'OE'}], [{'firstName': 'John', 'Age': 'D', 'Income': 'firsnew'}], [{'firstName': 'John', 'LASTNAME': 'DOlast_nameOE', 'Age': 35, 'cItY': 'new yochrrerryrok', 'Income': '$50,000', 'cItIY': 37}], [{'PI': 2.2762868739904514, 'new ryorrk': 1.7300435058060522, 'new ryorLast_Namerk': 2.6443947966293897}], [{'firstName': 'Johon', 'LASTNAME': 'DOE', 'Age': 'D', 'cItY': 'new yorAgek'}], [{'LASTNAME': 'DOE', 'Income': '$50,000', 'IncIome': 'FIRST_NAME', 'cItAgee': 'DOEnew yorAgeIncIomekIncome'}], [{'firstName': 'John', 'LASTNAME': 'DODE', 'cItY': 'new york'}], [{'first_name': 'John', 'Last_Name': 'Dooe', 'Age': 35, 'FIRST_NAME': 'Jane', 'CITY': 'Doe', 'yogrAgekk': 'Do$$50,000e', 'Last_eName': 'JanLast_Namee', 'cItIY': 'JafirstsNamee'}], [{'firstName': 'John', 'LASTNAME': '1DOE', 'Age': 'D', 'Income': 'YorkLASTcity_NAMEPI', 'AoraNewngege': 'JNew YorkLAST_NAMEPIohn'}], [{'LASTNAME': 'DOE', 'Age': 'D', 'cItY': 'FIRSTNAME', 'Income': '$50,000', 'IncIome': 'FIRST_NAME'}], [{'LASTNAME': 'DOE', 'Age': 'DIncIome', 'cItY': 'FIRSTNAME', 'Income': '$5DcItYnewOE0', 'IencIome': 'FINew YorkLAST_NALast_NammeMEPIRSTNAME'}], [{'firstName': 'John', 'LASTNAME': 'DOE', 'Income': '$50,000', '8': '$0,000', '$50,,000': '0$50,000'}], [{'LASTNAME': 'DOE', 'Age': 'D', 'cItY': 'new yorAgek', 'Income': '$50,000', 'LASTNAE': 'new yorAgeInDOfDOlasNew Yoincomerkt_nameEirstNameEcIomek', 'IncomNew YorkLAST_NAMEe': 'new yorA$0,000geIncIomrek'}], [{'firstName': 'Jooohn', 'LASTNAME': 'YorNke', 'cItY': '2', 'IncIome': 'FIRST_NAME', 'Anew yorAgek': 'FIRSTNNAME'}], [{'Age': 35, 'FIRST_NAME': 'Jane'}], [{'firstName': 'Johnew yorAgekhn', 'Age': 'D'}], [{'firstName': 'John', 'LASTNAME': 'D', 'Age': 'D', 'Income': 'YORK'}], [{'first_name': 'John', 'Last_Name': 'DYorNkoe', 'FIRST_NAME': 'cherry', 'Income': 'cyherry'}], [{'LASTNAME': 'DOE', 'Age': 'IPI', 'cItY': '2', 'IncIome': 'FIRfirstNam$50,0000eST_NAME'}], [{'LASTNAME': 'DOE', 'Age': 'D', 'cItY': 'nenew yorAgeIncIomekw 2$0,000yorAgek', 'IncIome': 'FIRST_NAME'}], [{'firstName': 'John', 'LASTNAME': 'DOE', 'Age': 35, 'Income': '$50,000', 'FIRST_NAME': 36, 'cItAGEY': 36}], [{'FIRST_NAME': 'John', 'AGE': 35, 'CITY': 'NEW YORK', 'YORK': '$50,00000'}], [{'LASTNAME': 'DOE', 'Income': '$50,000', 'IncIome': 'FIRST_NAME'}], [{'first_name': 'John', 'last_name': 'Doe', 'age': 36, 'city': 'New YorNk', 'income': 'bana', 'year': 37}], [{'33.803989620075356': 'D', '20.960571956786623': 'I', '-98.15414377148647': 'DOYorkLAST_NAMEPI', '0.8622214662877261': 'Zxdvjbw', '-48.45477875780888': 'yorAgeIncIomek', '2.6189164796316335': 'CqvytR', '2.1459305021091426': 'JafirstsNamee', '-21.558299894752437': 'DOE', '28.79129205112295': 'BEIHSKizc', '1.690316164828218': 'FXwMCxaHo'}], [{'first_name': 'John', 'Last_Name': 'color', 'Age': 35, 'Income': '$50,000', 'FIRST_NAME': 'Jane', '': 35, 'fruuit': 34}], [{'first_name': 'John', 'Age': 35, 'city': 'New York', 'Income': '$50,000', 'FIRST_NAME': 'Jane', '1': 36, 'Incyellowome': 'INCOMEJohn', '1chery': '$50,1DOE000'}], [{'LASTNAME': 'DOE', 'Income': '$50,000', 'IncIome': 'FIRST_NAME', 'new yorok': '2019n'}], [{'firstName': 'hJon', 'LASTNAME': 'DOE', 'Age': 35, 'Income': '$50,000', '8': 36, 'IP': 36}], [{'PI': 2.9360614575298136, 'new ryorrk': 1.7300435058060522, 'new ryorLast_Namerk': 2.6443947966293897, 'new ryorLast$50,000NNewYork_Namerk': 1.7300435058060522}], [{'firstName': 'John', 'LASTNAME': 'DOE', 'Age': 35, 'FIRST_NAME': 36, 'cItAGEY': 36, 'ageage': 36}], [{'orange': 'JoDooehn', 'LAST_NAME': 'NK'}], [{'first_name': 'Jonew yorAgekcolorhn', 'Last_Name': 'Doe', 'Age': 35, 'city': 'New York', 'Income': '$50,000', 'Incoome': 'kNew York'}], [{'LAST_NAME': 'oJoh', 'CITY': 'NK', '1': 35}], [{'firstName': 'Jooohn', 'LASTNAME': 'YorNke', 'cItY': '2', 'IncIome': 'FIRST_NAME', 'IncI$50,0000ome': '222'}], [{'firstName': 'Jooohn', 'LASTNAME': 'DOE', 'cItY': 'city', 'IncIome': 'FIRST_NAME', 'Anew yorAgek': 'FIRSTNAME'}], [{'LASTNAME': 'DOE', 'Age': 'IPI', 'cItY': '2', 'IncIome': 'FIRfirstNam$500,0000eST_NAME'}], [{'first_name': 'John', 'last_name': 'Doe', 'age': 36, 'city': 'New YorNk', 'income': 'bana', 'year': 38}], [{'first_name': 'John', 'Last_Name': 'Doe'}], [{'first_name': 'John', 'Age': 35, 'city': 'new yorAgek', 'Income': '$50,,000'}], [{'first_name': 'John', 'last_name': 'Doe', 'age': 35, 'city': 'New York', 'income': '$50,000', 'ageage': 'Dooe', 'new yorok': '8', 'Last_Name': 'chge'}], [{'firstName': 'John', 'LASTNAME': 'DOE', 'Income': '$50,000', 'IncIome': 'FIRST_NAME', 'I': 'yorAgeIncIomekw'}], [{'LAST_NAME': 'DOE', 'INCOME': '$50,000', 'Age': 37}], [{'city': 'N8ew York', 'FIRST_NAME': 'OE'}], [{'last_name': 'Doe', 'age': 35, 'city': 'New York', 'income': '$5Yoincomerkt_nameEirstNameEcIomek0,000', 'ageage': 'Inconme'}], [{'LASTNAME': 'DOE', 'Age': 'D', 'cItY': 'NewYork', 'Income': '$50,000', 'IncIome': 'FIRST_NAME'}], [{'first_name': 'John', 'Last_Name': 'color', 'Age': 35, 'Income': '$50,000', 'FIRST_NAME': 'Jane', '': 34, 'fruuit': 34}], [{'first_name': 'John', 'Age': 35, 'city': 'New York', 'Income': '$50,000', 'FIRST_NAME': 'nJane', '1': 36, 'Incyellowome': 'INCOMEJohn'}], [{'firstName': 'John', 'LASTNAME': 'DDOE', 'cItY': 'new yorAgek', 'Income': '$50,000', 'IncIome': 'cItAGEY', 'LASTENAME': 'Anew yorAgek'}], [{'1': 'apple', '2': 'banana', '3': 'cherry', 'Income': 'hJohn', '22': 'Johhn'}], [{'first_name': 'John', 'Age': 35, 'city': 'new yorAgek', 'Income': '$50,,000', 'FIRST_NAME': 'Jane', 'Anenew': 'oJohn'}], [{'firstName': 'JohaInconmege', 'Age': 35, 'cItY': 'new york', 'Incom': 'Yoincomerkt_nameEirstNameEcIomek'}], [{'firstName': 'John', 'Age': 'D', 'Income': 'YORK', 'Aege': 'nenew yorAgeIncIomekw yorAgek'}], [{'PI': 2.9360614575298136, 'new ryorrk': 1.7300435058060522, 'new ryorLast_Namerk': 2.6443947966293897, 'new ryorLast$50,000NNewYork_Namerk': 1.7300435058060522, 'IPI': 1.9949170779000351}], [{'first_name': 'John', 'Last_Name': 'Doe', 'city': 'new yorAgek', 'Income': '$50,000', 'FIRST_NAME': 'Jane', 'Dooe': 'firstNam$50,0000e'}], [{'3': 'cherry', 'Income': 'New York', '33': '8PI'}], [{'firstName': 'Jhohn', 'LASTNAME': 'DOE', 'Age': 'D', 'cItY': 'new yorAgekcolor', 'firstN': 'JohaJgeage', 'cItAGEY': 'JJoDooehhnohaJgeage'}], [{'firstName': 'John', 'LASTNAME': 'clor', 'Age': 'D', 'Income': 'YORK', 'year': 'Johnew yorAgekhn'}], [{'firstName': 'John', 'LASTNAME': 'DOE', 'cItY': 'new yorrk', 'Income': '$50,000', 'CITY': 'DOfDOlast_nameEirstNameE'}], [{'first_name': 'John', 'last_name': 'Doe', 'age': 35, 'income': '$50,000', 'new yorok': '8', 'DOcitiyE': 35}], [{'Age': 35, 'FIRST_NAME': 'yorAgeIncIomekw', 'yorok': 'yyorAgeIncIomekw'}], [{'first_name': 'John', 'Last_Name': 'Dooe', 'Age': 35, 'city': 'chery', 'Income': '$50,000', 'FIRST_NAME': 'Jane', '1': 36, 'Incyellowome': 'INCOMEJohn', 'chINCEOMEerryAge': '$50,00', 'chge': 'New YorkLAST_NAME', 'New York': 'new york', 'Incomge': 'citty', 'Last_eName': 'AGE'}], [{'first_name': 'John', 'Last_Name': 'Dooe', 'Age': 35, 'city': 'New York', 'Income': '$0,000', 'FIRST_NAME': 'Jane', '1': 37, 'Incyellowome': 'INCOMEJohn', 'IncIncYorkLASTcity_NAMEPIIomelowome': 'New YoJohageagek', 'IncIncYorkLASJanelowome': 'New', 'first_rname': 'Nehw YoJohageagek', 'FIRS222T_NAME': 'INCOMEJNohn'}], [{'city': 'N8ew York', 'FIRST_NAME': 'OE', 'citty': 'ONKE'}], [{'firstName': 'John', 'LASTNAME': 'DOE', 'Age': 35, 'Income': '$50,000', 'FIRST_NAME': 36, 'cItAGEY': 36, 'firrstName': 'chINCEOMEerryAnenew'}], [{'3': 'cherrfirstNy', '$50,000': 'chrerry', '$50,00NewNEWor$50,00ange0': 'age'}], [{'PI': 2.9360614575298136, 'new ryorrk': 1.7300435058060522, 'new ryorLast_Namerk': 2.6443947966293897, 'new ryorLast$50,000NNewYork_Namerk': 1.7300435058060522, 'IPI': 1.9949170779000351, 'firstNe': 3.14159}], [{'first_name': 'John', 'Last_Name': 'Dooe', 'Age': 35, 'city': 'New York', 'Income': '$50,000', 'FIRST_NAME': 'Anew', '1': 36, 'Incyellowome': 'INCOMEJohn', 'chINCEOMEerryAge': '$50,00', 'Incyelllowome': '$5YorNke0,000'}], [{'2': 'banana', '3': 'cherry', 'Income': 'chINCEOMEerry', 'or$50,00ange': 'bananAGEa'}], [{'first_name': 'John', 'Last_Name': 'Dooe', 'Age': 35, 'Income': '$50,000', 'FIRST_NAME': 'Jane', 'Incyellowome': 'INCOMEJohn', 'FIRSMT_NAME': 'Jan2,000e'}], [{'Dooe': 'fruuritt', 'Age': 'ffruuritt', 'Anew yorrk': '1'}], [{'orange': 'Jon', 'or$50,00ange': 'fruui'}], [{'first_name': 'John', 'Age': 35, 'city': 'YORKNewY York', 'Income': '$50,000', 'FIRST_NAME': 'Jane', 'Incom2019e': 'Joh2,000n'}], [{'1': 'apple', '2': 'banana', '3': 'Johhn'}], [{'firstName': 'Jooohn', 'LASTNAME': 'YorNke', 'cItY': '2', 'Anew yorAgek': 'FIRSTNAME'}], [{'first_name': 'John', 'Age': 35, 'city': 'new chINCEOMEOerryyorAgek', 'Income': '$50,000', 'FIRST_NAME': 'Jane'}], [{'FIRST_NAME': 'Jane', 'AAge': 'Jcherrohn'}], [{'first_name': 'John', 'Last_Name': 'Dooe', 'city': 'NK', 'FIRST_NAME': 'Jane', '1': 36, 'Incyellowome': 'INCOMEJohn', 'chINCEOMEerryAge': '$50,00'}], [{'firstName': 'John', 'LASTNAME': 'DOE', 'Age': 35, 'cItY': 'INCOME', 'Income': '$50,000', 'CITY': 'DOfDOlast_nameEirstNameE', 'NEW': '1'}], [{'first_name': 'John', 'Last_Name': 'Do', 'Age': 35, 'city': 'New York', 'Income': '$50,000', 'FIRST_NAME': 'Anew', '1': 36, 'Incyellowome': 'INCOMEJohn', 'chINCEOMEerryAge': '$50,00', 'Last_Namme': 'fruit', 'citiy': '8PI', 'FIRSTNAME': 38}], [{'Age': 35, 'Income': '$50,000'}], [{'PI': 3.14159, 'IPI': 2.6443947966293897, 'Johageage': 2.9360614575298136, 'PPI': 2.9360614575298136}], [{'FIRST_NAME': 'John', 'LAST_NAME': 'OE', 'AGE': 35, 'COME': '$50,0000', 'YORK': 'Anenew', 'Jcherrohn': 'chINCEOMEerryAnenew', 'chrerry': 'Anennew'}], [{'1': 'apple', '2': 'banana', '3': 'Johhn', 'Jonew yorAgekcolorhn': 'JohaInconmege'}], [{'firstName': 'Jhohn', 'LASTNAME': 'DOE', 'Age': 'D', 'cItY': 'YorNk', 'cItAGEY': 'JJoDooehhZxdvjbwnohaJgeage'}], [{'firstName': 'John', 'LASTNAME': 'DOE', 'Age': 'D', 'cItY': 'new yyork', 'fcityirstName': 'nAgeeew york'}], [{'firstName': 'John', 'LASTNAME': 'DOE', 'Age': 35, 'FIRST_NAME': 36, 'LASTE': 'cItY'}], [{'LASTNAME': 'DOE', 'cItY': '2', 'IncIome': 'FIRST_NAME', 'LASTNAMTE': 'Jonohn', 'N8ew York': 'Jocyherrynohn'}], [{'first_name': 'IncIomNNew', 'Last_Name': 'DYorNkoe', 'FIRST_NAME': 'OE'}], [{'LASTNAME': 'DOE', 'Age': 'D', 'cItY': 'nenew yorAgeIncIomekw yorAgek', 'IncIome': 'FIRST_NAME', 'eAge': '$50,000NNewYorkYoincomerk', 'AJan2,000ege': 'DD'}], [{'first_name': 'John', 'Age': 35, 'Income': '$50,,000'}], [{'LASTNAME': 'DOE', 'Age': 'D22', 'cItY': 'nenew yorAgeIncIomekw yorAgek', 'Income': '$50,000', 'IncIome': 'FIRST_NAME'}], [{'LASTNAME': 'DOE', 'Age': 'D', 'Income': '$50,000', 'IncIome': 'FIRST_NAME', 'IncIom': 'FINew YorkLAST_NALast_NammeMEPIRSTNAME'}], [{'LASTNAME': 'DOE', 'Age': 'I2', 'cItY': '2', 'InceIome': 'Last_Namme'}], [{'firstName': 'John', 'LASTNAME': 'DOE', 'Age': 'D', 'cItY': 'new yorAgek', 'Income': '$50,000', 'LASTN': 'DD'}], [{'2': 'banana', '2$0,000': 'chery'}], [{'Age': 35, 'city': 'New York', 'FIRST_NAME': 'nJane', '1': 36, 'Incyellowome': 'INCOMEJohn'}], [{'firstName': 'John', 'LASTNAME': 'DOE', 'Age': 'D', 'cItY': 'new yorAgek', 'Income': '$50,000', 'IncIomNNew YorkLASTcity_NAMEPIew Yorke': 'yorAgek'}], [{'LASTNAME': 'DOE', 'Age': 'D'}], [{'LASTNAME': 'DOE', 'Age': 'IPI', 'cItY': '2', 'Income': '$50,000', 'IncIome': 'FIRST_NAME', 'Do': 'EDOE', 'cItYJocyherrynohn': 'Joohn'}], [{'firstName': 'John', 'LASTNAME': 'DOE', 'Age': 'ONKE', 'Income': '$50,000'}], [{'firstName': 'Jooohn', 'LASTNAME': 'YorNke', 'cItY': '2', 'IncIome': 'yorAgeIncIomek', 'Anew yorAgek': 'FIRSTNAME', 'cIttY': 'JooohyorAgeIncIomekn'}], [{'LASTNAME': 'DOE', 'Age': 'IPI', 'cItY': '2'}], [{'first_name': 'John', 'Age': 36, 'city': 'new chINCEOMEOerryyorAgek', 'FIRST_NAME': 'Jane'}], [{'LASTNAME': 'YorNke', 'cItY': '2', 'IncIome': 'yorAgeIncIomek', 'Anew yorAgek': 'FIRSTNAME', 'cIttY': 'JooohyorAgeIncIomekn'}], [{'first_name': 'John', 'last_name': 'Doe', 'age': 37, 'city': 'New YorNk', 'income': 'bana'}], [{'firstName': 'John', 'LASTNAME': 'DOE', 'Age': 'D', 'Income': '$50,000', 'Ag': 'new y'}], [{'first_name': 'John', 'Last_Name': 'Dooe', 'Age': 35, 'city': 'New York', 'Income': '$50,000', 'FIRST_NAME': 'Jane', '1': 36, 'Incyellowome': 'INCOMEJohn', 'IncIncYorkLASTcity_NAMEPIIomelowome': 'New YoJohageagek', 'Last_e': 'Yoincomerk'}], [{'Last_Name': 'DYorNkoe', 'FIRST_NAME': 'cherry', 'Income': 'cyherry'}], [{'PI': 1.7300435058060522, 'New YorkLAST_NAMEPI': 2.6189164796316335, 'cItIY': 2.6443947966293897, 'New YorkLASTcity_NAMEPI': 2.3210819853008124, 'New YorkLAST_NPAMEPI': 1.3462361524091344, '$$50,000': 2.79480680351591}], [{'city': 'New York', 'FIRST_NAME': 'nJane', '1': 38, 'Incyellowome': 'INCOMEJohn'}], [{'LAST_NAME': 'oJoh', 'CITY': 'Anew yorrk', '1': 35}], [{'firstName': 'John', 'LASTNAME': 'DOE', 'cItY': 'new yorrk', 'CITY': 'DOfDOlast_nameEirstNameE'}], [{'LASTNAME': 'DOE', 'IncIome': 'FIRST_NAMIE', 'new yorok': '2019n'}], [{'LASTNAME': 'DOE', 'Age': 'IPI', 'IncIome': 'Anenew yorAgeIncIomekw yorAgek', 'Do': 'EDOE'}], [{'LASTNAME': 'DOE', 'Age': 'D', 'Income': '$50,000', 'IncIome': 'FIRST_NAME', 'IncomJohhne': 'DEOE'}], [{'firstName': 'John', 'LASTNAME': 'DOE', 'Age': 35, 'cItY': 'new yorok', 'Income': '$50,000', 'cItIY': 36, '2': 'Yk', 'cItIYY': 35}], [{'FIRST_NAME': '2019n', 'LAST_NAME': 'OE', 'AGE': 35, 'CITY': 'NEW YORK', 'COME': '$50,0000', 'LASTNAECOME': 37}], [{'firstName': 'John', 'LASTNAME': 'DOE', 'Age': 35, 'cItY': 'new yorok', 'Income': '$50,000', 'cItIY': 36, '2': 'Yk', 'cItIYY': 35, 'cItIYYnew ryorrk': 'Yk2,000'}], [{'LASTNAME': 'DOE', 'Age': 'D22', 'cItY': 'nenew yorAgeIncIomekw yorAgek', 'Income': '$50,000', 'IncIome': 'FIRST_NAME', 'CyellOMEcItY': 'chge', 'cIctY': 'DOE33'}], [{'first_name': 'John', 'Last_Name': 'Doe', 'city': 'New Yrork', 'Income': '$50,000', 'FIRST_NAME': 'Jane'}], [{'last_name': 'Doe', 'age': 35, 'city': 'AoraNewngegeNew York', 'income': '$5Yoincomerkt_nameEirstNameEcIomek0,000', 'ageage': 'Inconme', 'LASTENAMEage': '$5Yoincomerkt_nameEirsttNameEcIomek0,000'}], [{'first_name': 'John', 'Age': 35, 'city': 'New York', 'Income': '$50,000', 'FIRST_NAME': 'Jane', '1': 36, 'Incyellowome': 'INCOMEJohn', '1chery': '$50,1DOE000', 'DOEnew yorAgeIncIomekIncome': 'ONKE'}], [{'2': 'banana', '3': 'cherry', 'Income': 'chINCEOMEerry', 'Incomge': 'new yorAgeIncIomek'}], [{'first_name': 'John', 'Age': 35, 'city': 'New York', 'Income': '$50,000', '1': 36, 'Incyellowome': 'INCOMEJohn', 'cityyorA$0,000geIncIomrek': 'JJohn'}], [{'Age': 'IPI', 'IncIome': 'FIRfirstNam$500,0000eST_NAME'}], [{'firstName': 'JohnoNew YorNk', 'LASTNAME': 'DDOE', 'Income': '$50,000', 'IncIome': 'FIRST_NAME', 'DIncome': 'YorkLASTcity_NAMEPIew'}], [{'LASTNAME': 'DOE', 'IncIome': 'FIRST_NAME', 'cItAgee': 'DOEnew yorAgeIncIomekIncome'}], [{'firstName': 'John', 'LASTNAME': 'DOlast_nameOE', 'Age': 35, 'cItY': 'new yochrrerryrok', 'cItIY': 37}], [{'first_name': 'John', 'Age': 36, 'Income': '$50,,000'}], [{'PI': 3.14159, 'Johageage': 2.9360614575298136, 'JohaJgeage': 3.14159}], [{'firstName': 'Johhn'}], [{'first_name': 'John', 'Last_Name': 'Doe', 'city': 'new yorAgek', 'Income': '$50,000', 'FIRST_NAME': 'Jane', 'DDOEIncome': '$50,00'}], [{'first_name': 'John', 'Age': 35, 'city': 'new chINCEOMEOerryyorAgek', 'Income': '$50,000', 'FIRST_NAME': 'Jane', 'Jonew': 'new chINCEOMEOeoDDOErangerryyorAgek'}], [{'first_name': 'John', 'Last_Name': 'Dooe', 'Age': 35, 'Income': '$50,000', 'FIRST_NAME': 'Jacityne', 'Incyellowome': 'INCOMEJohn'}], [{'firstName': 'Johnbana', 'Age': 'D', 'Income': 'KYORK'}], [{'first_name': 'John', 'Last_Name': 'Doe', 'city': 'new yorAgek', 'Income': '$50,000', 'FIRST_NAME': 'Jane', 'DDOEIncome': '$50,00', 'citcy': '$50,00New YorkLAST_NALast_NammeMEPI0'}], [{'first_name': 'Yk2,000', 'Last_Name': 'Do', 'Age': 35, 'city': 'New York', 'Income': '$50,000', 'FIRST_NAME': 'Anew', '1': 36, 'Incyellowome': 'INCOMEJohn', 'chINCEOMEerryAge': '0$50,00', 'Last_Namme': 'fruit', 'citiy': '8PI'}], [{'PI': 1.7300435058060522, 'New YorkLAST_NAMEPI': 1.2679847915686973, 'cItIY': 2.6443947966293897, 'New YorkLASTcity_NAMEPI': 2.3210819853008124}], [{'firstName': 'John', 'LASTNAME': 'DOE', 'Age': 'D', 'IncIome': 'FIRST_NAME'}], [{'Last_Name': 'Doe', 'Age': 36, 'city': 'New York', 'Income': '$50,000', 'Incoome': 'kNew York', 'AAge': 'cIttY'}], [{'orange': 'JoDooehn', 'okNewrange': 'INCOMEJJohn', 'orangae': 'YorkLAST_NALast_NammeMEPI0JoDooehn'}], [{'first_name': 'John', 'Last_Name': 'Dooe', 'Age': 35, 'city': 'New York', 'Income': '$50,000', 'FIRST_NAME': 'Anew', '1': 36, 'Incyellowome': 'INCOMEJohn', 'chINCEOMEerryAge': '$50,$00', 'Last_Namme': 'fruit'}], [{'LASTNAME': 'DOE', 'Age': 'IPI', 'cItY': '2', 'yogrAgek': 'YorkSTNAME'}], [{'first_name': 'IncIomNNew', 'Last_Name': 'DYorNkoe', 'city': 'NewCyellOME York', 'FIRST_NAME': 'ODOlast_nameOEE'}], [{'first_name': 'John', 'Last_Name': 'Doe', 'city': 'New York', 'FIRST_NAME': 'cherry', 'ryorrk': 'Jnohn'}], [{'LASTNAME': 'DOE', 'Age': 'yorAgeIncIomekw', 'Income': '$500,000', 'IncIome': 'FIRST_NAME', 'Incomeyeyar': 'AAge'}], [{'last_name': 'Doe', 'age': 35, 'city': 'New York', 'income': '$5Yoincomerkt_namAneneweEirstNameEcIomek0,000', 'ageage': 'Inconme'}], [{'first_name': 'John', 'Last_Name': 'Dooe', 'Age': 35, 'Income': '$50,000', 'FIRST_NAME': 'Jane', '1': 36, 'Incyellowome': 'INCOMEJohn', 'IncIncYorkLASTcity_NAMEPIIomelowome': 'New YoJohageagek', 'Last_e': 'Yoincomerk'}], [{'first_name': 'John', 'Last_Name': 'Doe', 'city': 'new yorAgek', 'Income': '$5Yoincomerkt_nameEirstNameEcIomek0,000', 'FIRST_NAME': 'Jane', 'Dooe': 'firstNam$50,0000e'}], [{'$50,000': 'chrerry', 'Inconme': 'bana'}], [{'first_name': 'John', 'Last_Name': 'Doe', 'Age': 35, 'city': 'new yorAgek', 'Income': '$50,000', 'FIRST_NAME': 'Jane', 'DDOEIncome': '$50,00', 'citty': 38}], [{'2': 'banana', '3': 'cherry'}], [{'firstName': 'John', 'LASTNAME': 'DOE', 'Age': 35, 'cItY': 'IencIome', 'Income': '$50,00FIRSTNNAME0', 'CITY': 'DOfDOlast_nameEirstNambananAGEaeE'}], [{'first_name': 'John', 'Last_Name': 'Doe', 'new yorrk': '8'}], [{'2': 'banana', '2$0,000': 'chery', 'orYoincomerk$50,00ange': 'yochrrerryrok'}], [{'PI': 2.9360614575298136, 'new ryorrk': 1.7300435058060522, 'new ryorLast_Namerk': -21.558299894752437, 'new ryorLast$50,000NNewYork_Namerk': 1.7300435058060522, 'IPI': 1.9949170779000351}], [{'firstName': 'John', 'LASTNAME': 'DOE', 'cItY': 'new yorAgek', 'Income': '$50,000'}], [{'LASTNAME': 'DOE', 'Age': 35, 'Income': '$50,000', 'FIRST_NAME': 36, 'cItAGEY': 36, 'firrstName': 'w'}], [{'first_name': 'John', 'Last_Name': 'Doe', 'city': 'NNew YorkLASTcity_NAMEPIew York', 'tfirst_name': '2JohJIncomeyeyarohnn', 'Last_Naeme': 'DoYorke'}], [{'firstName': 'yorAgekcolorhnJohhn'}], [{'first_name': 'John', 'Last_Name': 'Dooe', 'Age': 35, 'Last_eName': 'JanLast_Namee', 'cItIY': 'JafirstsNamee'}], [{'firstName': 'hJon', 'LASTNAME': 'DOE', 'Age': 35, '8': 36, 'IP': 36}], [{'firstName': 'Jooohn', 'LASTNAME': 'YorNke', 'IncIome': 'yorAgeIncIomek', 'Anew yorAgek': 'FIRSTNAME'}], [{'PI': 1.7300435058060522, 'New YorkLAST_NAMEPI': 2.6189164796316335, 'cItIY': 2.6443947966293897, 'I': 2.496132463875833, 'CyellOME': 1.6243371737850312}], [{'1': 'aple', '2': 'banana', 'Income': 'chINCEOMEerry', 'CITY3': 'cherr'}], [{'orange': 'fruurit', 'or$50,00ange': 'fruui', 'orYoincomerk$50,00ange': 'fruYoincomerkuritt'}], [{'firstName': 'John', 'LASTNAME': 'DDOE', 'cItY': 'new yorAgek', 'Income': '$50,000', 'IncIome': 'cItAGEY'}], [{'PI': 1.7300435058060522, 'New YorkLAST_NAMEPI': 2.6189164796316335, 'cItIY': 2.6443947966293897, 'I': 1.4713856995958976, 'CyellOME': 1.6243371737850312}], [{'PI': 1.7300435058060522, 'cItIY': 2.6443947966293897, 'New YorkLAST_NALast_NammeMEPI': 0.17904925194593924, 'New YorkLALASTENAMEageST_NALast_NammeMEPI': 2.2786871475765835}], [{'FIRST_NAME': 'John', 'AGE': 35, 'YORK': '$50,00000'}], [{'FIRST_NAME': 'John', 'LAST_NAME': 'OE', 'AGE': 35, 'CITY': 'NEW YORK', 'YORK': '$50,00000', 'FIRFIRSTNAMEAME': '$ryorLast_Namerk50,00000'}], [{'orange': 'JoDooehn'}], [{'firstName': 'John', 'Age': '0$50,00', 'Income': 'YORK', 'Aege': 'nenew yorAgeIncIomekw yorAgek'}], [{'3': 'cherry', 'Income': 'chINCEOMEerry', 'Inncome': 'chINCffruurittEOMEerry'}], [{'firstName': 'John', 'cItY': 'new yorrk', 'Income': '$50,000', 'CITY': 'DOfDOlasNew Yoincomerkt_nameEirstNameE'}], [{'LASTNAME': 'YorNke', 'cItY': '2', 'IncIome': 'FIRST_NAME', 'IncI$50,0000ome': '222'}], [{'PI': 0.9299554777703931, 'cItIY': 2.6443947966293897, 'New YorkLAST_NALast_NammeMEPI': 0.17904925194593924, 'New YorkLALASTENAMEageST_NALast_NammeMEPI': 2.2786871475765835}], [{'first_name': 'John', 'Last_Name': 'Doe', 'Income': 'color', 'Dooe': 'firstNam$50,0000e'}], [{'first_name': 'John', 'Age': 36, 'Income': '$50,,000', 'Aege': 35}], [{'first_name': 'Johnn', 'Last_Name': 'Doe', 'Income': 'color'}], [{'first_name': 'John', 'Last_Name': 'DYorNkoe', 'FIRST_NAME': 'cherry', 'Last_Namme': 'yeyar', 'LasYorkLAST_NALast_NammeMEPI0t_Namme': 'yer'}], [{'-27.654576852346665': 'uYc', '41.671200125445324': 'orange', '12.66919465416403': 'VNxJOt', '-42.16356333079692': 'new yorAgeInDOfDOlasNew Yoincomerkt_nameEirstNameEcIomek', '46.77667061964502': 'Last_Naeme', '-29.856800477994057': 'DIncIome', '1.9949170779000351': 'QxxTRMjexO'}], [{'FIRST_NAME': 'John', 'AGE': 35, 'CITY': 'NEW YcIctYORK', 'YORK': '$50,00000'}], [{'firstName': 'John', 'LASTNAME': 'DOE', 'cItY': 'new yorAgek', 'Income': '$50,000', 'firstNfame': 'new yorAgekcolor'}], [{'first_name': 'Jonew yorAgekcolorhn', 'Last_Name': 'Doe', 'Age': 35, 'city': 'New York', 'Incoome': 'kNew York'}], [{'first_name': 'John', 'last_name': 'Doe', 'age': 35, 'city': 'oNNew YorNk', 'income': 'DD', 'Newage': '2,000'}], [{'first_name': 'John', 'Age': 35, 'Income': '$50,000', 'FIRST_NAME': 'Jane', 'Incyellowome': 'YorNk00', 'CITY': 'Doe', 'yogrAgekk': 'Do$$50,000e'}], [{'Last_Name': 'Doe'}], [{'firstName': 'John', 'LASTNAME': 'DOE', 'Age': 'IP', 'Income': '$50,000', 'IncIome': 'FIRST_NAME', 'eAge': 'FIRSJhohnT_NAME'}], [{'last_name': 'Doe', 'age': 35, 'city': 'New YorNk', 'income': '$50,000', 'chINCffruurittEOMEerry': '$5Yoincomerkt_nameEirstNameEcIomek0,000'}], [{'PI': 1.7300435058060522, 'New YorkLAST_NAMEPI': 2.6189164796316335, 'cItIY': 1.4094949772734846, 'I': 2.7107068449059466}], [{'firstName': 'John', 'LASTNAME': 'DDOE', 'Age': 'D', 'cItY': 'new yorAgek', 'Income': '$50,000', 'IncIome': 'FIRST_NAME', 'LASTENAME': 'Anew yorAgek', 'IncYorkLASTcity_NAMEPIIome': 'Anenew yorAgeIncIomekw yorAgek', 'ageage': 'cItYnew yorAgek', '2019n': 'IPI', '12019n': 'DJohnew yorAgekhn'}], [{'first_name': 'John', 'Age': 35, 'city': 'New York', 'Income': '$0,000', 'FIRST_NAME': 'Jane', '1': 37, 'Incyellowome': 'INCOMEJohn', 'IncIncYorkLASTcity_NAMEPIIomelowome': 'New YoJohageagek'}], [{'first_name': 'John', 'Age': 35, 'city': 'new chINCEOMEOerryyorAgek', 'FIRST_NAME': 'Jane'}], [{'firstName': 'John', 'LASTNAME': 'DOE', 'Age': 36, 'Income': '$50,000', '8': 'chINCEOMEOerryyorAgek', 'firslast_nametName': 'cherry', '': 'apple'}], [{'Age': 'D', 'cItY': 'nenew yorAgeIncIomekw 2$0,000yorAgek'}], [{'1': 'apple', '2': 'tfirst_name', 'Income': 'hJohn', '22': 'Johhn'}], [{'LASTNAME': 'DOE', 'Age': 'IPI', 'cItY': 'new yorAgek', 'Income': '$5Yoincomerkt_nameEirstNameEcIomek0,000', 'IncIome': 'FIRST_NAME', 'firsnew yorAgektName': 'new yogrAgek', 'ccItAGEYItY': 'new yogrAgekk'}], [{'PI': 1.7300435058060522, 'New YorkLAST_NAMEPI': 2.6189164796316335, 'cItIY': 2.6443947966293897, 'New YorkLASTcity_NAMEPI': 2.3210819853008124, 'ccItIY': 2.9039294830493683}], [{'FIRST_NAME': 'John', 'LAST_NAME': 'DOE', 'AGE': 35, 'CITY': '33K', 'INCOME': '$50,000', '1': 35, 'INOECOME': '$$50,000'}], [{'first_name': 'John', 'Last_Name': 'INCOMEJNohn', 'Age': 35, 'city': 'New York', 'Income': '$50,000', 'FIRST_NAME': 'Jane', '1': 36, 'Incyellowome': 'INCOMEJohn', 'chINCEOMEerryAge': '$50,00', 'Newor$50,00ange': 'NNewYork'}], [{'FIRST_NAME': 'John', 'LAST_NAME': 'DOE', 'AGE': 35, 'INCOME': '$50,000', 'LAScItIYYnewT_NAME': 'cyherry'}], [{'Age': 35, 'FIRST_NAME': 'Jane', 'firstNam$50,0000e': 38, 'DOfDOlast_nameEirstNambananAGEaeE': 35}], [{'Last_Name': 'Dooe', 'Age': 35, 'city': 'New York', 'Income': '$50,000', 'FIRST_NAME': 'Jane', '1': 36, 'Incyellowome': 'INCOMEJohn', 'chINCEOMEerryAge': '$50,00'}], [{'LAST_NAME': 'oJoh', 'AGE': 35, 'CITY': 'NK', '1': 34, 'AE': ''}], [{'first_name': 'John', 'city': 'new yorAgek', 'Income': '$50,,000', 'ncome': 35}], [{'firstName': 'John', 'LASTNAME': 'DOE', 'cItY': 'new york'}], [{'firstName': 'John', 'LASTNAME': 'DOE', 'Age': 36, 'Income': '$50,000', '8': '$0,000', '222': '$york'}], [{'PI': 3.14159, 'IPI': 2.6443947966293897, 'JohaJgeage': 3.14159, 'PPI': 2.9360614575298136, 'PPDDOEI': 1.8117899160754405}], [{'FIRST_NAME': 'John', 'COME': '$50,0000', 'John': 'year', 'yorrk19': 'yellow', 'income': 'yelelow', 'yorrk1': 'orangae'}], [{'FIRST_NAME': 'Jane', 'AAge': 'Jchenrrohn'}], [{'first_name': 'John', 'Age': 35, 'Income': '$50,000', '1': 36, 'Incyellowome': 'INCOMEJohn', 'cityyorA$0,000geIncIomrek': 'JJohn'}], [{'firstName': '$50,000NNewYorkYoincomerkyorAgekkcolorhnJohhn'}], [{'PI': 3.14159, 'IPI': 2.6443947966293897, 'Johageage': 3.7806371669520606, 'JohaJgeage': 3.14159}], [{'3': 'cheryrfirstNy', '$50,000': 'chrerry', '$50,00NewNEWor$50,00ange0': 'age'}], [{'orange': 'fruurit', 'or$50,00ange': 'fruui', 'orYoincomerk$50,00ange': 'fruuritt', 'or$50,00ang': 'frageuui'}], [{'first_name': 'John', 'Last_Name': 'Doe', 'Age': 35, 'city': 'Newor$50,00ange York', 'Income': 'nenew yorAgeIncIomekw 2$0,000yorAgek', 'FIRST_NAME': 'Jane', 'Incoome': 'oJohn', '': 'oJoh'}], [{'PI': 2.2762868739904514, 'new ryorrk': 1.7300435058060522, 'new ryorLast_Namerk': 2.6443947966293897, 'new ryYrorkorLast_Namerk': -48.45477875780888}], [{'FIRST_NAME': 'Jane', 'AAge': 'Jcherrohn', '$50,000NNewYorkYoincomerk': 'IencIome', 'new yogrAgekk': 'JcherrocItYJocyherrynohnhn'}], [{'first_name': 'John', 'Last_Name': 'Dooee', 'Age': 35, 'Income': 'tfirst_name', 'FIRST_NAME': 'Jane', 'Incyellowome': 'INCOMEJohn', 'first_namme': '$50,0last_name00'}], [{'firstName': 'John', 'LASTNAME': 'DOE', 'Age': 36, 'Income': '$50,000', '8': '$0,000', 'IncoDDOErangeome': '$550,000'}], [{'Agee': 35}], [{'2': 'VNxJOt', 'Income': 'New York'}], [{'firstName': 'hJohn', 'LASTNAME': 'DOE', 'Age': 35, 'Income': '$50,000', '8': '$0,000', 'LASTNAAME': 'citcy'}], [{'first_name': 'John', 'Age': 35, 'city': 'New York', 'Income': 'Dooe', 'FIRST_NAME': 'Jane', '1': 37, 'Incyellowome': 'INCkNew YorkOMEJohn', 'chINCEOMEerryAge': '$50,00', 'firsnew yorAgektName': 'new yorAgeIncIomekIncome', 'citty': 'Jon'}], [{'first_name': 'John', 'Last_Name': 'Dooe', 'Age': 35, 'city': 'New York', 'Income': '$50,000', 'FIRST_NAME': 'Jane', '1': 36, 'Incyellowome': 'INCOMEJohn', 'IncIncYorkLASTcity_NAMEPIIomelowome': 'New YoJohageagek', 'Last_e': 'Yoincomerk', 'Incyellowe': 'Jancherre'}], [{'3': 'cherry'}], [{'LASTNAME': 'DOE', 'Age': 'D', 'IncIome': 'FIRST_NAME', 'IncomJohhne': 'DEOE'}], [{'firstName': 'John', 'LASTNAME': 'DOE', 'Age': 'D', 'Income': '$50,000', 'Ag': 'new y', 'firstJohJIncomeyeyarohnnName': 'JYORKNewYohn'}], [{'AGE': 36, 'INCOME': '$50,000', 'Age': 35}], [{'first_name': 'John', 'Age': 36, 'city': 'new yorAgek', 'FIRST_NAME': '33K', 'Anenew': 'oJohn', 'Inme': 'oJoJhn'}], [{'first_name': 'John', 'Last_Name': 'Doe', 'Age': 35, 'city': 'New York', 'Income': '$50,000', 'FIRST_NAME': 'Jane', 'firAEst_name': 'JaJne'}], [{'first_name': 'John', 'Age': 35, 'city': 'new yorAgek', 'FIRST_NAME': 'Jane'}], [{'first_name': 'John', 'Age': 35, 'Income': '$50,000', 'FIRST_NAME': 'Jane', 'Incyellowome': 'YorNk00', 'CITY': 'Doe', 'yogrAgekk': 'Do$$50,000e', 'AyorAgek': 35}], [{'first_name': 'John', 'Last_Name': 'Dooe', 'Age': 35, 'city': 'New York', 'Income': '$50,000', 'FIRST_NAME': 'Jane', '1': 36, 'Incyellowome': 'INCOMEJohn', 'IncIncYorkLASTcity_NAMEPIIomelowome': 'New YoJohageagek', 'Last_e': 'Yoincomerk', 'Incyellowe': 'JYORKNewYohn'}], [{'IncIome': 'FIRST_NAMIE', 'new yorok': '2019n'}], [{'Last_Name': 'Do', 'Age': 35, 'city': 'New York', 'Income': '$50,000', 'FIRST_NAME': 'Anew', '1': 36, 'Incyellowome': 'INCOMEJohn', 'chINCEOMEerryAge': '$50,00', 'Last_Namme': 'fruit', 'fDOlast_nameEirstName': 'NNewYork', 'Nehw': 'PPnew chINCEOMEOerryyorAgekI'}], [{'yellow': 'color', 'yell': 'clor', 'yellowAnenew': 'YorNk'}], [{'firstName': 'Jooohn', 'Anew yorAgek': 'FNIRSTNAME'}], [{'last_name': 'Doe', 'age': 35, 'city': 'New York', 'cit': 35}], [{'first_name': 'John', 'Last_Name': 'Dooee', 'Age': 35, 'Income': 'tfirst_name', 'FIRST_NAME': 'Jane', 'Incyellowome': 'INCOMEJohn', 'first_namme': '$50,0last_name00', 'Aclor': 'INCOMEJLANewYohn'}], [{'1': 'apple', '2': 'orange', '3': 'cherry', 'Income': 'chINCEOMEerry', 'banana2': 'chINCEEOMEerry'}], [{'LASTNAME': '8PI', 'cItY': '2', 'IncIome': 'yorAgeIncIomek', 'Anew yorAgek': 'FIRSTNAME', 'cIttY': 'JooohyorAgeIncIomekn', 'IncIocme': 'JoDooehhn'}], [{'first_name': 'IncIomNNew', 'FIRST_NAME': 'OE'}], [{'LAST_NAME': 'oJoh', 'AGE': 35, 'CITY': 'NK', '1': 34, 'AE': 'new', 'QxxTRMjexO': 'oJhoh', 'TCITY': 34}], [{'firstName': 'John', 'LASTNAME': 'DOE', 'Age': 'D', 'cItY': 'new yorAgek', 'Income': '$50,000', 'IncIome': 'FIRST_NAME', 'LASTENAME': 'Anew yorAgek', 'cItcY': 'DD'}], [{'FIRST_NAME': 'John', 'AGE': 35, 'CITY': 'NEW YORK', 'INCOME': '$50,000', 'INCNewT_NAMEPIOME': 'NEW'}], [{'Last_Name': 'Dooe', 'Age': 35, 'city': 'chery', 'Income': '$50,000', 'FIRST_NAME': 'Jane', '1': 36, 'Incyellowome': 'INCOMEJohn', 'chINCEOMEerryAge': '$50,00', 'chge': 'New YorkLAST_NAME', 'New York': 'new york', 'Incomge': 'citty', 'Last_eName': 'AGE'}], [{'firstName': 'yorAgekcoJoDo$$50,000ehageagelorhnJohhn'}], [{'LASTNAME': 'DOE', 'cItY': '2', 'Income': '$50,000', 'IncIome': 'FIRST_NAME', 'Do': 'EDOE'}], [{'Income': '$50,000'}], [{'or$50,00ange': 'fruui', 'orYoincomerk$50,00ange': 'fruuritt'}], [{'firstName': 'JohDOE33', 'LASTNAME': 'DDOE', 'Income': '$50,0000'}], [{'first_name': 'John', 'Last_Name': 'Doe', 'Age': 35, 'city': 'NewNEWor$50,00ange York', 'Income': '$50,000', 'FIRST_NAME': 'eJane', 'Incoome': 'oJohn', 'Agee': '$50,0oNew YorNk00'}], [{'firstName': 'John', 'LASTNAME': 'DOE', 'Age': 35, 'Income': '$50,000', 'FIRST_NAME': 36, 'LASTNASME': 'oJohn'}], [{'first_name': 'John', 'city': 'New York', 'Income': '$50,000', '1': 36, 'Incyellowome': '2$0,000', 'cityyorA$0,000geIncIomrek': 'JJohn'}], [{'firstName': 'NNew', 'LASTNAME': 'DDOE', 'Income': '$50,0000', 'IncIome': 'FIRST_NAME'}], [{'firstName': 'John', 'LASTNAME': 'DOE', 'Age': 35, 'cItY': 'new yorrk', 'Income': '$50,000', 'CITY': 'DOfDOlast_nameEirstNameE', 'NEW': '1', 'ge': 'nNew YorkLAST_NPAMEPIew yorrk'}], [{'last_name': 'new yorrkoe', 'age': 36, 'city': 'New YorNk', 'income': 'bana', 'year': 37}], [{'first_name': 'John', 'city': 'new yorAgek', 'ncome': 35}], [{'first_name': 'John', 'last_name': 'Doe', 'age': 35, 'city': 'oNew YorNk', 'income': '$50,000', 'Newage': '2,000', 'first_nam': 'JohnDOfDOlasNew Yoincomerkt_nameEirstNameE'}], [{'first_name': 'John', 'Age': 36, 'city': 'New York', 'Income': '$50,000', 'FIRST_NAME': 'Jane'}], [{'first_name': 'John', 'Age': 36, 'city': 'new yorAgek', 'FIRST_NAME': '33K', 'Anenew': 'oJohn', 'Inme': 'oJoJhn', 'Yrork': 'oJoJhkNewn'}]]
    results = [True, False, False, False, True, True, False, True, True, False, False, False, True, False, True, False, True, False, False, False, False, False, True, False, False, False, True, False, False, True, False, False, True, False, True, False, False, False, False, False, False, True, False, True, False, False, True, False, False, False, False, False, True, False, False, False, False, False, True, False, False, False, False, False, False, True, False, False, True, False, True, False, False, False, True, False, False, False, False, True, False, False, False, False, False, True, False, False, False, False, False, False, True, False, False, False, False, False, True, False, False, False, True, False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, False, True, False, False, False, False, False, False, True, True, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, True, True, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, True, False, False, True, False, True, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, True, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, True, True, True, False, False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, True, True, False, False, False]
    for i, (inp, exp) in enumerate(zip(inputs, results)):
        assertion(candidate(*inp), exp, 0)


check(check_dict_case)