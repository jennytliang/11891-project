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

    def strength(s):
        c = 0
        for char in s:
            if char.isupper() or char == '_':
                c += 1
        d = 0
        for char in s:
            if char.islower() or char == '_':
                d += 1
        return (c-d)

    return f'{class_name}.{min([d for i, d in enumerate([strength(n) for n in extensions]) if d >= 0]) < 0 else [c for c in extensions if sorted([strength(n) for n in extensions])[0] == strength(c)][0]}'