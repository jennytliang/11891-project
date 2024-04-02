def Strongest_Extension(class_name, extensions):
    """You will be given the name of a class (a string) and a list of extensions.
    The extensions are to be used to load additional classes to the class. The
    strength of the extension is as follows: Let CAP be the number of the uppercase
    letters in the extension's name, and let SM be the number of lowercase letters 
    in the extension's name, the strength is given by the fraction CAP - SM. 
    You should find the strongest extension and return a string in this 
    format: ClassName.StrongestExtensionName.
    If there are two or more extensions with the same strength, you should
    choose the one that comes first in the list.
    For example, if you are given "Slices" as the class and a list of the
    extensions: ['SErviNGSliCes', 'Cheese', 'StuFfed'] then you should
    return 'Slices.SErviNGSliCes' since 'SErviNGSliCes' is the strongest extension 
    (its strength is -1).
    Example:
    for Strongest_Extension('my_class', ['AA', 'Be', 'CC']) == 'my_class.AA'
    
	Include these tokens in the code: def strength ( s : str ) -> int :
	"""

    # create a dictionary for the extensions
    strengths = {}
    for i in extensions:
        cap = 0
        sm = 0
        for j in i:
            if j.isupper():
                cap += 1
            elif j.islower():
                sm += 1
            else:
                pass
        strengths[i] = cap - sm

    # find the strongest extension
    strongest = max(strengths, key=strengths.get)

    # return the strongest extension
    return "{}.{}".format(class_name, strongest)


# print(Strongest_Extension("my_class", ["AA", "Be", "CC"]))
# print(Strongest_Extension("my_class", ["AA", "Be", "CCCC"]))
# print(Strongest_Extension("my_class", ["AA", "Be", "CC", "cC"]))
# print(Strongest_Extension("my_class", ["AA", "Be", "CC", "cC", "dd"]))
# print(Strongest_Extension("my_class", ["AA", "Be", "CC", "cC", "dd", "EE"]))
# print(Strongest_Extension("my_class", ["AA", "Be", "CC", "cC", "dd", "EE", "FF"]))
# print(Strongest_Extension("my_class", ["AA", "Be", "CC", "cC", "dd", "EE", "FF", "gg"]))
# print(Strongest_Extension("my_class", ["AA", "Be", "CC", "cC", "dd", "EE", "FF", "gg", "HH"]))
# print(Strongest_Extension("my_class", ["AA", "Be", "CC", "cC", "dd", "EE", "FF", "gg", "HH", "ii"]))
# print(Strongest_Extension("my_class", ["AA", "Be", "CC", "cC", "dd", "EE", "FF", "gg", "HH", "ii", "JJ"]))