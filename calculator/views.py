from django.shortcuts import render
from .models import Student, Semester
from .forms import StudentForm
from .utils import calculate_gpa, calculate_cgpa
from decimal import Decimal


def student_form(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            matric_no = form.cleaned_data['matric_no']
            name = form.cleaned_data['name']
            semester1_grades = form.cleaned_data['semester1_grades']
            semester1_course_units = form.cleaned_data['semester1_course_units']
            semester2_grades = form.cleaned_data['semester2_grades']
            semester2_course_units = form.cleaned_data['semester2_course_units']

            student = Student.objects.create(matric_no=matric_no, name=name)

            semester1 = Semester.objects.create(student=student, semester_number=1,
                                                grades=semester1_grades,
                                                course_units=semester1_course_units)
            semester2 = Semester.objects.create(student=student, semester_number=2,
                                                grades=semester2_grades,
                                                course_units=semester2_course_units)

            print(f"Semester 1 Grades: {semester1_grades}")
            print(f"Semester 1 Course Units: {semester1_course_units}")
            print(f"Semester 2 Grades: {semester2_grades}")
            print(f"Semester 2 Course Units: {semester2_course_units}")

            # Calculate GPAs
            if semester1_grades != '' and semester1_course_units != '':
                semester1_grades = semester1_grades.split(', ')
                semester1_course_units = [int(unit) for unit in semester1_course_units.split(',')]

            if semester2_grades != '' and semester2_course_units != '':
                semester2_grades = semester2_grades.split(', ')
                semester2_course_units = [int(unit) for unit in semester2_course_units.split(',')]

            semester1_gpa = round(calculate_gpa(semester1_grades, semester1_course_units), 2)
            semester2_gpa = round(calculate_gpa(semester2_grades, semester2_course_units), 2)

            print(f"Semester 1 GPA: {semester1_gpa}")
            print(f"Semester 2 GPA: {semester2_gpa}")

            # Calculate CGPA
            if semester1_gpa is not None and semester2_gpa is not None:
                cgpa = calculate_cgpa([semester1_gpa, semester2_gpa],
                                      semester1_course_units + semester2_course_units)
                if cgpa is not None:
                    cgpa = round(Decimal(cgpa), 2)
            else:
                cgpa = None

            print(f"CGPA: {cgpa}")

            return render(request, 'result.html', {
                'name': name,
                'matric_no': matric_no,
                'semester1_gpa': semester1_gpa,
                'semester2_gpa': semester2_gpa,
                'cgpa': cgpa,
            })
        else:
            # Print form errors for debugging
            print(form.errors)

    else:
        form = StudentForm()

    return render(request, 'student_form.html', {'form': form})
