def calculate_gpa(grades, course_units):
    # Mapping of grades to corresponding grade points
    grade_points = {
        'A': 4.0,
        'B': 3.0,
        'C': 2.0,
        'D': 1.0,
        'F': 0.0,
    }

    total_grade_points = 0
    total_course_units = 0

    for i in range(len(grades)):
        grade = grades[i]
        course_unit = course_units[i]

        if grade in grade_points:
            grade_point = grade_points[grade]
            total_grade_points += grade_point * course_unit
            total_course_units += course_unit

    if total_course_units == 0:
        return None

    gpa = total_grade_points / total_course_units
    return gpa



def calculate_cgpa(gpas, course_units):
    total_gpa_points = 0
    total_course_units = 0

    for i in range(len(gpas)):
        gpa = gpas[i]
        course_unit = course_units[i]

        total_gpa_points += gpa * course_unit
        total_course_units += course_unit

    if total_course_units == 0:
        return None

    cgpa = total_gpa_points / total_course_units
    return cgpa

