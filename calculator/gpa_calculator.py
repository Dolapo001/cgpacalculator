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

    for grade, units in zip(grades, course_units):
        if grade in grade_points:
            grade_point = grade_points[grade]
            total_grade_points += grade_point * units
            total_course_units += units

    if total_course_units == 0:
        return None

    gpa = total_grade_points / total_course_units
    return gpa
