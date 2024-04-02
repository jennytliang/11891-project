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
    
	Include these tokens in the code: def to _ letter _ grade ( score ):
	"""

    grade_list = []

    for i in grades:
        if i >= 4.0:
            grade_list.append("A+")
        elif i >= 3.7:
            grade_list.append("A")
        elif i > 3.3:
            grade_list.append("A-")
        elif i > 3.0:
            grade_list.append("B+")
        elif i > 2.7:
            grade_list.append("B")
        elif i > 2.3:
            grade_list.append("B-")
        elif i > 2.0:
            grade_list.append("C+")
        elif i > 1.7:
            grade_list.append("C")
        elif i > 1.3:
            grade_list.append("C-")
        elif i > 1.0:
            grade_list.append("D+")
        elif i > 0.7:
            grade_list.append("D")
        elif i > 0:
            grade_list.append("D-")
        else:
            grade_list.append("E")
    
    """    
a = 5
grade = 3.6 

while a == 5:
    if grade >= 4.0:
        grade_list.append("A+")
    elif grade >= 3.7:
        grade_list.append("A")
    elif grade > 3.3:
        grade_list.append("A-")
    elif grade > 3.0:
        grade_list.append("B+")
    elif grade > 2.7:
        grade_list.append("B")
    elif grade > 2.3:
        grade_list.append("B-")
    elif grade > 2.0:
        grade_list.append("C+")
    elif grade > 1.7:
        grade_list.append("C")
    elif grade > 1.3:
        grade_list.append("C-")
    elif grade > 1.0:
