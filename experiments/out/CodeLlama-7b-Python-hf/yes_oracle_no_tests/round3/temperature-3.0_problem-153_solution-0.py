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
    # First, we get the strongest extension
    strongest_ext = extensions[0]
    strongest_strength = strength(strongest_ext)
    for ext in extensions:
        ext_strength = strength(ext)
        if ext_strength > strongest_strength:
            strongest_ext = ext
            strongest_strength = ext_strength
    # Then we return the string
    return class_name + '.' + strongest_ext


def strength(s):
    cap = 0
    sm = 0
    for c in s:
        if c.isupper():
            cap += 1
        elif c.islower():
            sm += 1
        else:
            pass
    return cap - sm


print(Strongest_Extension('my_class', ['AA', 'Be', 'CC']))
