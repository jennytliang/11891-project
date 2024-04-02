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
    
	Include these tokens in the code: def to
	Do not include these tokens in the code: output = [] for each
	"""
    

    grade_gpa_dict={
        "A+": 4.0,
        "A": 3.7,
        "A-": 3.3,
        "B+": 3.0,
        "B": 2.7,
        "B-": 2.3,
        "C+": 2.0,
        "C": 1.7,
        "C-": 1.3,
        "D+": 1.0,
        "D": 0.7,
        "D-": 0.0,
        "E": 0.0
    }
    grades_letters = [ "A+", "A", "A-", "B+", "B", "B-", "C+", "C", "C-", "D+", "D", "D-", "E"]
    
    def numerical_grades(listGrades):
        numerialGrades=[] 
        for _ in listGrades: 
            numerialGrades.append("{:.2f}".format(float(_)))
        
        return numerialGrades
    
    print(numerical_grades([4.0, 3, 1.7, 2, 3.5]))
    
    #Return a list of grade
    def letter_grade(listGrades):
        numerial_grades = numerical_grades(listGrades)
        numerial_grades = map(float (),numerial_grades)
        
        grade_string=[]

        for _ in numerial_grades: 
            for k, v in grade_gpa_dict.items(): 
                if _ > v: 
                    grade_string.append(k)
                    
        return grade_string    
    