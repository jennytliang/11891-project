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
    def letter_grade(grades):
        letter_grade_list = []
        for score in grades:
            if score >= 4.0:
                letter_grade_list.append("A+")
            elif score >= 3.7:
                letter_grade_list.append("A")
            elif score >= 3.3:
                letter_grade_list.append("A-")
            elif score >= 3.0:
                letter_grade_list.append("B+")
            elif score >= 2.7:
                letter_grade_list.append("B")
            elif score >= 2.3:
                letter_grade_list.append("B-")
            elif score >= 2.0:
                letter_grade_list.append("C+")
            elif score >= 1.7:
                letter_grade_list.append("C")
            elif score >= 1.3:
                letter_grade_list.append("C-")
            elif score >= 1.0:
                letter_grade_list.append("D+")
            elif score >= 0.7:
                letter_grade_list.append("D")
            elif score >= 0.0:
                letter_grade_list.append("D-")
            else:
                letter_grade_list.append("E")
        return letter_grade_list
    return letter_grade(grades)

def test_function(test_case):
    grades = test_case[0]
    solution = test_case[1]
    output = numerical_letter_grade(grades)
    for index, value in enumerate(output):
        if value == solution[index]:
            print("Pass")
        else:
            print("Fail")

test_function([[4.0, 3, 1.7, 2, 3.5], ["A+", "B", "C-", "C", "A-"]])
test_function([[2.0, 1.5, 1.0, 0.5, 0.0], ["C+", "C", "D", "