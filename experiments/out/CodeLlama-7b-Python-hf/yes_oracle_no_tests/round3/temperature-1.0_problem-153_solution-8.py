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
    max_strength = 0
    max_ext = ''
    
    for ext in extensions:
        cap_letters = 0
        small_letters = 0
        
        for c in ext:
            if c.isupper():
                cap_letters += 1
            elif c.islower():
                small_letters += 1
            else:
                continue
                
        strength = cap_letters - small_letters
        
        if strength >= max_strength:
            max_strength = strength
            max_ext = ext
    
    return class_name + '.' + max_ext


# Strongest_Extension('my_class', ['AA', 'Be', 'CC']) == 'my_class.AA'
# Strongest_Extension('my_class', ['AA', 'Be', 'CC', 'DD']) == 'my_class.DD'
# Strongest_Extension('my_class', ['AA', 'aA', 'aa']) == 'my_class.AA'
# Strongest_Extension('my_class', ['AA', 'a', 'aa']) == 'my_class.AA'
# Strongest_Extension('my_class', ['AA', 'A', 'aa']) == 'my_class.AA'
# Strongest_Extension('my_class', ['AA', 'A', 'a']) == 'my_class.A'
# Strongest_Extension('my_class', ['AA', 'Aa', 'A']) == 'my_class.A'
# Strongest_Extension('my_class', ['AA', 'Aa', 'a']) == 'my_class.A'
# Strongest_Extension('my_class', ['AA', 'Aa', 'aa']) == 'my_class.Aa'
# Strongest_Extension('my_class', ['AA', 'Aa', 'AA']) == 'my_class.AA'
# Strongest_Extension('my_class', ['Aa', 'AA', 'AA']) == 'my_class.AA'
# Strongest_Extension('my_class', ['Aa', 'AA', '