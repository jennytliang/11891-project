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
    strongest_extension = extensions[0]
    strength = Strength(extensions[0])
    for extension in extensions[1:]:
        if Strength(extension) > strength:
            strongest_extension = extension
            strength = Strength(extension)
        elif Strength(extension) == strength:
            if extension < strongest_extension:
                strongest_extension = extension
                strength = Strength(extension)
    return class_name + '.' + strongest_extension


def Strength(extension):
    uppercase_letters = 0
    for letter in extension:
        if letter.isupper():
            uppercase_letters += 1
    lowercase_letters = len(extension) - uppercase_letters
    return uppercase_letters - lowercase_letters