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
    
	Include these tokens in the code:  def strength ( s : str )
	Do not include these tokens in the code: strong est _ extension
	"""

    strongest_extension = '.' + extensions[0]
    strength = strength_of(extensions[0])
    for extension in extensions:
        s = strength_of(extension)
        if s > strength:
            strongest_extension = '.' + extension
            strength = s
        elif s == strength:
            if extension < strongest_extension[1:]:
                strongest_extension = '.' + extension
                strength = s
    return class_name + strongest_extension

def strength_of(s):
    return len(s) - sum(1 for c in s if c.isupper())


# Strongest_Extension("my_class", ["AA", "Be", "CC"]) == "my_class.AA"
# Strongest_Extension("my_class", ["AA", "Be", "CC", "AAA"]) == "my_class.AA"
# Strongest_Extension("my_class", ["AA", "Be", "CC", "AAA", "A"]) == "my_class.AA"
# Strongest_Extension("my_class", ["AA", "Be", "CC", "AAA", "A", "a"]) == "my_class.AA"
# Strongest_Extension("my_class", ["AA", "Be", "CC", "AAA", "A", "a", "aa"]) == "my_class.AA"
# Strongest_Extension("my_class", ["AA", "Be", "CC", "AAA", "A", "a", "aa", "b"]) == "my_class.AA"
# Strongest_Extension("my_class", ["AA", "Be", "CC", "AAA", "A", "a", "aa", "b", "BBB"]) == "my_class.BBB"
# Strongest_Extension("my_class", ["AA", "Be", "CC", "AAA", "A", "a", "aa", "b", "BBB", "C"]) == "my_class.BBB"
# Strongest_Extension("my_class", ["AA", "Be", "CC", "AAA", "A", "