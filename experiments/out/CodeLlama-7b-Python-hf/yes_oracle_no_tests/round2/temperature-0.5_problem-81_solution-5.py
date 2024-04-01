def numerical_letter_grade(grades):
    """It is the last week of the semester and the teacher has to give the grades
    to students. The teacher has been making her own algorithm for grading.
    The only problem is, she has lost the code she used for grading.
    She has given you a list of GPAs for some students and you have to write 
    a function that can output a list of letter grades using the following table:
             GPA       |    Letter grade
              4.0                A+
            > 3.7                A 
            > 3.3                A- 
            > 3.0                B+
            > 2.7                B 
            > 2.3                B-
            > 2.0                C+
            > 1.7                C
            > 1.3                C-
            > 1.0                D+ 
            > 0.7                D 
            > 0.0                D-
              0.0                E
    

    Example:
    grade_equation([4.0, 3, 1.7, 2, 3.5]) ==> ['A+', 'B', 'C-', 'C', 'A-']
    
	Include these tokens in the code: score
	Do not include these tokens in the code: grade
	"""



    def to_letter_grade(gpa):
        if gpa > 4:
            return "A+"
        elif gpa > 3.7:
            return "A"
        elif gpa > 3.3:
            return "A-"
        elif gpa > 3:
            return "B+"
        elif gpa > 2.7:
            return "B"
        elif gpa > 2.3:
            return "B-"
        elif gpa > 2:
            return "C+"
        elif gpa > 1.7:
            return "C"
        elif gpa > 1.3:
            return "C-"
        elif gpa > 1:
            return "D+"
        elif gpa > 0.7:
            return "D"
        elif gpa > 0.3:
            return "D-"
        else:
            return "E"

    return [to_letter_grade(g) for g in grades]


def evaluate(a, b):
    return lambda x: a*x**2 + b*x

def find_roots(f, a, b):
    """
    f is a function
    a and b are numbers
    returns: a list of all the roots of f between a and b
    """
    rts = []
    x = a
    while x < b:
        if f(x) == 0:
            rts.append(x)
        x += 0.1
    return rts


def find_roots_better(f, a, b):
    """
    f is a function
    a and b are numbers
    returns: a list of all the roots of f between a and b
    """
    rts = []
    x = a
    while x < b:
        if f(x) == 0:
            rts.append(x)
        x += 0.01
    return rts


def find_roots_betterer(f, a, b):
    """
    f is a function
    a and b are numbers