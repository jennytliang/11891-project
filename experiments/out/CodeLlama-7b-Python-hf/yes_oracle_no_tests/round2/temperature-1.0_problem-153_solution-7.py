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

    if len(extensions) == 0:
        return(class_name)
    s_ext = []
    for ext in extensions:
        cap = 0
        sm = 0
        for _ in ext:
            if _.isupper():
                cap = cap + 1
            elif _.islower():
                sm = sm + 1
            """
            strength = cap - sm
            if len(s_ext) == 0:
                s_max = strength
                s_ext.append(ext)
            elif strength > s_max:
                s_ext = [ext]
                s_max = strength
            elif strength == s_max:
                s_ext.append(ext)
            """
        s_ext.append((cap, sm, ext))

    s_ext.sort(reverse=True)
    return(class_name+"."+s_ext[0][2])


if __name__ == '__main__':
    print("Example:")
    print(Strongest_Extension('my_class', ['AA', 'Be', 'CC']))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert Strongest_Extension('my_class', ['AA', 'Be', 'CC']) == 'my_class.AA', "Strength of my_class.AA is 1"
    assert Strongest_Extension('my_class', ['AAA', 'Be', 'CCC']) == 'my_class.AAA', "Strength of my_class.AAA is 0"
    assert Strongest_Extension('my_class', ['AA', 'Be', 'CCC']) == 'my_class.CCC', "Strength of my_class.CCC is -1"
    assert Strongest_Extension('my_class', ['aBc', 'Be', 'CC']) == 'my_class.CC', "Strength of my_class.CC is -2"
    print("Coding complete? Click 'Check' to earn cool rewards!")