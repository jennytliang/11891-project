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
    strongest = extensions[0]
    strength = strength(extensions[0])
    for ext in extensions[1:]:
        if strength(ext) > strength(strongest):
            strongest = ext
    return class_name + '.' + strongest


def strength(s):
    return len([c for c in s if c.isupper()]) - len([c for c in s if c.islower()])


# Best Practices
def strength(s):
    return s.upper().count('') - s.lower().count('')
